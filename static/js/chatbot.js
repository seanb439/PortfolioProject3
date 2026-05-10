// Chatbot functionality
function toggleChatbot() {
    const body = document.getElementById('chatbotBody');
    if (body.style.display === 'none') {
        body.style.display = 'flex';
        document.getElementById('chatInput').focus();
        // Add welcome message if chat is empty
        const messages = document.getElementById('chatMessages');
        if (messages.children.length === 0) {
            addBotMessage("Hello! I'm here to help answer questions about Sean's portfolio. Feel free to ask about projects, skills, experience, or anything else!");
        }
    } else {
        body.style.display = 'none';
    }
}

function sendMessage() {
    const input = document.getElementById('chatInput');
    const message = input.value.trim();

    if (message === '') return;

    // Add user message to chat
    addUserMessage(message);
    input.value = '';

    // Get CSRF token from meta tag or cookie
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value || getCookie('csrftoken');

    // Send to backend
    fetch('/api/chatbot/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ message: message })
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            addBotMessage(data.response);
        })
        .catch(error => {
            console.error('Error:', error);
            addBotMessage('Sorry, I encountered an error. Please try again.');
        });
}

function addUserMessage(message) {
    const messagesDiv = document.getElementById('chatMessages');
    const messageElement = document.createElement('div');
    messageElement.className = 'chat-message user';
    messageElement.textContent = message;
    messagesDiv.appendChild(messageElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function addBotMessage(message) {
    const messagesDiv = document.getElementById('chatMessages');
    const messageElement = document.createElement('div');
    messageElement.className = 'chat-message bot';
    messageElement.textContent = message;
    messagesDiv.appendChild(messageElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function handleChatInput(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
