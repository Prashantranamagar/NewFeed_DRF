from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

LANG = [
    ('Nepali', 'NEP'),
    ('English', 'ENG')
]

class Source(models.Model):
    name = models.CharField(max_length=100, null=True, )
    source_url = models.TextField()
    language = models.CharField(max_length=10, null = True, choices=LANG, default='Nepali')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'source'
        ordering = ['-created_at']
        verbose_name = _("Source")
        verbose_name_plural = _("Sources")

    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name =  models.CharField(max_length=100, null=True)
    icon = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        ordering = ['-created_at']
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    
    def __str__(self):
        return self.name
    

class NewsFeed(models.Model):
    title = models.TextField(blank=True)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True, blank=True)
    category_1 = models.TextField(null=True, blank=True)
    category_2 = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    published_date = models.CharField(null=True, max_length=500, blank=True)
    short_description = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # Fields for your model here
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.created_by = User.objects.first()  # Set the created_by field to the logged-in user
    #     self.updated_by = User.objects.first()  # Set the updated_by field to the logged-in user
    #     super().save(*args, **kwargs)

    # @classmethod
    # def create(cls, **kwargs):
    #     instance = cls(**kwargs)
    #     instance.save()
    #     return instance

    class Meta:

        db_table = 'news_feed'
        ordering = ['-created_at']
        verbose_name = _("NewsFeeds")
        verbose_name_plural = _("NewsFeeds")

    def __str__(self):
        return self.title


 
    


