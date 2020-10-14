from rest_framework import serializers

from .models import File, Check

class FileSerializer(serializers.ModelSerializer):

  class Meta():
    model = File
    fields = ('file', 'name', 'timestamp')

class CheckSerializer(serializers.ModelSerializer):

  class Meta():
    model = Check
    fields = ('file' , 'timestamp')