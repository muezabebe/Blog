from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    pub_date = models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=255,null=True)
    content = models.TextField()
    photo=models.ImageField(null=True,blank=True,upload_to="images/")
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):

        return f'(pub_date: {self.pub_date}) (title:{self.title}) (content: {self.content})(author:{self.author})'














