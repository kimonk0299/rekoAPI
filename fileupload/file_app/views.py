from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .functions import upload, check, save 
from .serializers import FileSerializer, CheckSerializer
from django.conf import settings
from django.http import JsonResponse
import os 

class FileView(APIView):

  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):

    check_serializer = CheckSerializer(data=request.data)
    if check_serializer.is_valid():
      #save file locally  
      check_serializer.save()   
      filenme = check_serializer.data.get("file")
      media_root = settings.MEDIA_ROOT
      location = (media_root.rpartition('/')[0]+filenme)

      #upload to s3 bucket and check 
      upload(str(location),'kimonktest')
      [similarity,searchname] = check('kimonktest',location.rpartition('/')[-1], "kishore_collection")

      #remove image loacally 
      os.remove(location)
      if (not similarity):
        identified = False
        searchname = ''
      else:
        identified = True
      return JsonResponse({
        "identified" : identified,
        "userdata": None,
        "name": searchname,
        "person_id":None ,
        "company_name":None ,
        "visitor_phone_no":None ,
        "visitor_email":None,
        "face_attr": '',
        "recommendation": {
                }
              })     
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileSave(APIView):

  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):

    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():

      # save file to server 
      file_serializer.save()   
      filenme = file_serializer.data.get("file")
      facename = file_serializer.data.get("visitor_name")
      visitor_name = file_serializer.data.get("visitor_name")
      company_name = file_serializer.data.get("company_name")
      whom_to_meet = file_serializer.data.get("whom_to_meet")
      visitor_phone_no = file_serializer.data.get("visitor_phone_no")
      visitor_email = file_serializer.data.get("visitor_email")
      media_root = settings.MEDIA_ROOT
      location = (media_root.rpartition('/')[0]+filenme)

      #upload media to s3 bucket and train 
      save (str(location),'kimonktest',facename)

      #removing local copy of image
      os.remove(location)
      return JsonResponse ({
        'Trained' : True,
        'visitor_name': visitor_name,
        'company_name': company_name,
        'whom_to_meet': whom_to_meet,
        'visitor_phone_no': visitor_phone_no,
        'visitor_email': visitor_email
        })
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)