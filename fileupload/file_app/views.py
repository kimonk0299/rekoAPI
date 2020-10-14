from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .functions import upload, check, save 
from .serializers import FileSerializer
from django.conf import settings
from django.http import JsonResponse

class FileView(APIView):

  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):

    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()   
      filenme = file_serializer.data.get("file")
      media_root = settings.MEDIA_ROOT
      location = (media_root.rpartition('/')[0]+filenme)
      upload(str(location),'kimonktest')
      [similarity,searchname] = check('kimonktest',location.rpartition('/')[-1], "kishore_collection")
      if (not similarity):
        print('not found')
        return Response('Notfound')
      else:
        return Response([similarity,searchname])     
      return (hello)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileSave(APIView):

  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):

    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()   
      filenme = file_serializer.data.get("file")
      media_root = settings.MEDIA_ROOT
      location = (media_root.rpartition('/')[0]+filenme)
      save (str(location),'kimonktest')
      return Response ('Face has been saved')
      # upload(str(location),'kimonktest')
      # [similarity,searchname] = check('kimonktest',location.rpartition('/')[-1], "kishore_collection")
      # if (not similarity):
      #   print('not found')
      #   return Response('Notfound')
      # else:
      #   return Response([similarity,searchname])     
      # return (hello)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)