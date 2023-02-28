from rest_framework import serializers
from .models import NewsFeed, Source
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model() 

class NewsFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsFeed
        fields = ['id', 'title', 'source', 'category_1', 'published_date', 'short_description', 'image_url', 'link']
          
        
    def create(self, data):
        #Check if the data already exist in the database
        existing_data = NewsFeed.objects.filter(title = data['title']).first()
        print("++++++++++++++++++++++",self.context['request'].user)
        if existing_data:
            return existing_data
        else:
            # obj  = NewsFeed.objects.create(**data)
            
            data['created_by'] = self.context['request'].user
            data['updated_by'] = self.context['request'].user
            print(data['created_by'])
            # Create new data if it doesn't exis t in the databases
            
            return NewsFeed.objects.create(**data)


    def update(self, instance, validated_data):
        validated_data['updated_by'] = self.context['request'].user
        return super().update(instance, validated_data)

class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = ['id', 'name', 'source_url', 'language']
          

