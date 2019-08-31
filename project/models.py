

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models
from django.db.models import signals as model_signals
from django.db.models.base import ModelBase
from django.db import models
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass




class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='عنوان')
    description = RichTextField(verbose_name='مطلب')
    user = models.ForeignKey(User,blank=True, null=True,verbose_name='نویسنده',on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True,verbose_name='عکس')
    date = models.DateField(auto_now_add=True)
    journal = 'jo'
    paper = 'pa'
    news = 'ne'
    programs = 'pr' 
    CHOICES = [
    (journal, 'مجله'),
    (paper, 'مقاله'),
    (news, 'اخبار'),
    (programs, 'نرم افزار'),
]
    kind = models.CharField(max_length=2, choices = CHOICES, default = paper,verbose_name = 'نوع مطلب')

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'id': self.pk})

    def __str__(self):
        return f'{self.title}--{str(self.date)}'





class PostFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d",verbose_name='فایل ها')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)