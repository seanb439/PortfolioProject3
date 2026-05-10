from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    description = models.TextField()
    category = models.CharField(max_length=100)
    business_problem = models.TextField()
    tools_used = models.CharField(max_length=500)
    key_features = models.TextField()
    role_contribution = models.TextField()
    challenge = models.TextField()
    lessons_learned = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    proficiency = models.CharField(
        max_length=50,
        choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Expert', 'Expert')]
    )
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    is_current = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.title} at {self.company}"
