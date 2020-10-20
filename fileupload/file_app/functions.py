import logging
import boto3
from botocore.exceptions import ClientError


def upload (file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name.rpartition('/')[-1]

    # Upload the file
    s3_client = boto3.client('s3','ap-south-1', aws_access_key_id='AKIASZCBCLLMFVT22NER', aws_secret_access_key='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')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        #add_collection(bucket,object_name,"kishore_collection",object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def save (file_name, bucket, image_id,object_name=None):
    def add_collection (bucket, key, collection_id,image_id):
        def index_faces(bucket, key, collection_id, image_id=None, attributes=(), region="ap-south-1"):
            rekognition = boto3.client("rekognition", region, aws_access_key_id='AKIASZCBCLLMFVT22NER', aws_secret_access_key='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')
            response = rekognition.index_faces(
                Image={
                    "S3Object": {
                        "Bucket": bucket,
                        "Name": key,
                    }
                },
                CollectionId=collection_id,
                ExternalImageId=image_id,
                DetectionAttributes=attributes,
            )
            return response['FaceRecords']

        for record in index_faces(bucket, key, collection_id, image_id):
            face = record['Face']

    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name.rpartition('/')[-1]

    # Upload the file
    s3_client = boto3.client('s3','ap-south-1', aws_access_key_id='AKIASZCBCLLMFVT22NER', aws_secret_access_key='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')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        add_collection(bucket,object_name,"kishore_collection",image_id)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def check (bucket, key, collection_id):

    def search_faces_by_image(bucket, key, collection_id, threshold=80, region="ap-south-1"):
        rekognition = boto3.client("rekognition", region, aws_access_key_id='AKIASZCBCLLMFVT22NER', aws_secret_access_key='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')
        response = rekognition.search_faces_by_image(
            Image={
                "S3Object": {
                    "Bucket": bucket,
                    "Name": key,
                }
            },
            CollectionId=collection_id,
            FaceMatchThreshold=threshold,
        )
        return response['FaceMatches']
    
    search = search_faces_by_image(bucket, key, collection_id)

    if (search == []):
        return [False,False]
    
    else:
        for record in search:
            face = record['Face']
            return([record['Similarity'], face['ExternalImageId']])
