from django.db import models

# Create your models here.
class Writer(models.Model):
    name=models.TextField()
    email=models.EmailField(unique=True)
    age=models.TextField()

    def __str__(self):
        return f"{self.name},{self.email}"
    
    
class Blog(models.Model):
    title= models.TextField()
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(Writer,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.title},{self.content},{self.published_at},{self.writer}"
    