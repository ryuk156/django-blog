from django.db import models

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    
    title=models.CharField(max_length=255)
    slug=models.CharField(max_length=255)
    content=models.TextField()
    link=models.TextField()
    image=models.FileField(upload_to='static')
    timestamp=models.DateTimeField(  blank= True)



    def __str__(self):
        return 'post from '+ self.title