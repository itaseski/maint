from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, verbose_name='Url', unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Published')
    image = models.ImageField(upload_to='blog/images/', null=True, blank=True)
    views = models.IntegerField(default=0, verbose_name="Viewed")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['-created_at']


