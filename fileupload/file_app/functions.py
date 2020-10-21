import boto3
from PIL import Image

def compress (location):
    foo = Image.open(location)
    (i,j) = foo.size
    
    ## find optimal compress size
    lo = 1
    hi = 10
    avg = (i+j)//2

    while(lo < hi):
        mid = lo + ((hi-lo)//2)
        if (avg//mid < 400):
            hi = mid 
        else:
            lo = mid+1

    i= i//lo 
    j= j//lo

    foo = foo.resize((i,j),Image.ANTIALIAS)
    foo.save(location,quality=95,optimize=True)

def save (photo,collection_id,name,phone):

    with open (photo, 'rb') as source_image:
        source_bytes = source_image.read()

    def index_faces(source_bytes, collection_id, image_id=None, attributes=(), region="ap-south-1"):
        rekognition = boto3.client("rekognition", region, aws_access_key_id='AKIASZCBCLLMFVT22NER', aws_secret_access_key='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')
        response = rekognition.index_faces(
            Image={
                'Bytes':source_bytes
            },
            CollectionId=collection_id,
            ExternalImageId=image_id,
            DetectionAttributes=attributes,
        )
        return response['FaceRecords']

    image_id = name+'-'+str(phone)
    for record in index_faces(source_bytes,collection_id, image_id):
        face = record['Face']


def check (photo,collection_id):

    with open (photo, 'rb') as source_image:
        source_bytes = source_image.read()

    def search_faces_by_image(source_bytes, collection_id, threshold=80, region="ap-south-1"):
        rekognition = boto3.client("rekognition", region, aws_access_key_id='AKIASZCBCLLMFVT22NER', aws_secret_access_key='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')
        response = rekognition.search_faces_by_image(
            Image={
                'Bytes':source_bytes
            },
            CollectionId=collection_id,
            FaceMatchThreshold=threshold,
        )
        return response['FaceMatches']
    
    search = search_faces_by_image(source_bytes, collection_id)

    if (search == []):
        return [False,False]
    
    else:
        for record in search:
            face = record['Face']
            return([record['Similarity'], face['ExternalImageId']])
