from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .functions import upload, check, save 
from .serializers import FileSerializer, CheckSerializer
from django.conf import settings
from django.http import JsonResponse

class FileView(APIView):

  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):

    check_serializer = CheckSerializer(data=request.data)
    if check_serializer.is_valid():
      check_serializer.save()   
      filenme = check_serializer.data.get("file")
      media_root = settings.MEDIA_ROOT
      location = (media_root.rpartition('/')[0]+filenme)
      upload(str(location),'kimonktest')
      [similarity,searchname] = check('kimonktest',location.rpartition('/')[-1], "kishore_collection")
      if (not similarity):
        print('not found')
        return JsonResponse({'Face Match' : False})
      else:
        return JsonResponse({'Confidence score':similarity, 'Name': searchname})     
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
      facename = file_serializer.data.get("remark")
      print('facename:', facename)
      media_root = settings.MEDIA_ROOT
      location = (media_root.rpartition('/')[0]+filenme)
      save (str(location),'kimonktest',facename)
      return JsonResponse ({'Face Train': True})
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