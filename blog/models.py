from django.db import models
from ckeditor.fields import RichTextField
from category.models import Genre, Device
from author.models import AuthorInfo



def SmallPosterPath(instance, filename):
    name = instance.title.replace(' ','-')
    filename = filename.replace(' ','-')
    return 'Blogs/Images/{0}/{1}'.format(name,filename)

def SliderPosterPath(instance, filename):
    name = instance.title.replace(' ','-')
    filename = filename.replace(' ','-')
    return 'Blogs/Images/{0}/{1}'.format(name,filename)

def BigPosterPath(instance, filename):
    name = instance.title.replace(' ','-')
    filename = filename.replace(' ','-')
    return 'Blogs/Images/{0}/{1}'.format(name,filename)

class Blog(models.Model):
    Genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True)
    AuthorInfo = models.ForeignKey(AuthorInfo, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    small_poster = models.ImageField(upload_to=SmallPosterPath)
    big_poster = models.ImageField(upload_to=BigPosterPath)
    slider_poster = models.ImageField(upload_to=SliderPosterPath)
    brif = models.TextField()
    descriptions = RichTextField()
    article = RichTextField()
    tags = models.CharField(max_length=500)

    URL = models.CharField(max_length=255, unique=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_descriptions = RichTextField()

    def __str__(self):
         return self.title



class ReleaseChoices(models.IntegerChoices):
    Null = 0 ,
    InTheMoment = 1 ,
    Scheduled = 2 , 

class BlogReports(models.Model):
    Blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    release = models.IntegerField(default=ReleaseChoices.Null , choices=ReleaseChoices.choices)
    like = models.IntegerField()
    dislike = models.IntegerField()
    view = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Reports"
        verbose_name_plural = "Reports"

    def __str__(self):
         return self.Blog.title


class BlogTag(models.Model):
    name = models.CharField(max_length=50)
    numberOfUsed = models.IntegerField(default=1)
    numbOfClicked = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
         return self.name





