from rest_framework import serializers

from .models import File, Check

class FileSerializer(serializers.ModelSerializer):

  class Meta():
    model = File
    fields = ('file', 'visitor_name','company_name','whom_to_meet','visitor_phone_no','visitor_email','timestamp')

class CheckSerializer(serializers.ModelSerializer):

  class Meta():
    model = Check
    fields = ('file' , 'timestamp')