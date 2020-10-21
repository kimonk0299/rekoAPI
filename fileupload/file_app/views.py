from rest_framework.views import APIView
from rest_framework.response import Response
from .functions import check, save, compress 
from .serializers import FileSerializer, CheckSerializer
from django.conf import settings
from django.http import JsonResponse
import os 

class FileView(APIView):

  def post(self, request, *args, **kwargs):
    request.data['file'] = request.data['image']
    check_serializer = CheckSerializer(data=request.data)
    print(request.data)

    if check_serializer.is_valid():
      #save file locally  
      check_serializer.save()   
      filenme = check_serializer.data.get("file")
      media_root = settings.MEDIA_ROOT
      location = (media_root.rpartition('/')[0]+filenme)

      #compress picture
      compress(location)

      #check similarity 
      [similarity,searchname] = check(str(location), "kishore_collection")
      txt = searchname.split("-")
      nameid= txt[0]
      phone_id = txt[1]


      #remove image loacally 
      os.remove(location)

      if (not similarity):
        identified = False
        searchname = ''
      else:
        identified = True
      return JsonResponse({
        "identified" : identified,
        "userdata": '(type: Visitor), (category: Enabled)',
        "name": nameid,
        "person_id":'ab69026f-bc03-447a-a362-2eeb4d3e6545' ,
        "id": 104,
        "company_name":'' ,
        "visitor_phone_no":phone_id , 
        "visitor_email":'',
        "face_attr": '',
        "recommendation": {
                }
              })     
    else:
      return Response('error')

class FileSave(APIView):

  def post(self, request, *args, **kwargs):

    request.data['file'] = request.data['image']
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():

      # save file to server 
      file_serializer.save()   
      filenme = file_serializer.data.get("file")
      facename = file_serializer.data.get("visitor_name")
      visitor_name = file_serializer.data.get("visitor_name")
      #company_name = file_serializer.data.get("company_name")
      #whom_to_meet = file_serializer.data.get("whom_to_meet")
      visitor_phone_no = file_serializer.data.get("visitor_phone_no")
      #visitor_email = file_serializer.data.get("visitor_email")
      media_root = settings.MEDIA_ROOT
      location = (media_root.rpartition('/')[0]+filenme)

      #compress picture
      compress(location)

      #upload media and train 
      save (str(location),"kishore_collection",facename,visitor_phone_no)

      #removing local copy of image
      os.remove(location)
      return JsonResponse ({
        'Trained' : True,
        'visitor_name': visitor_name,
        #'company_name': company_name,
        #'whom_to_meet': whom_to_meet,
        'visitor_phone_no': visitor_phone_no,
        #'visitor_email': visitor_email
        })
    else:
      return Response('error')