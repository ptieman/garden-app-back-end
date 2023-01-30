from rest_framework import serializers
from .models import JournalEntry, SeedList, User, ToDoList

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = '__all__'
        
class SeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeedList
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'