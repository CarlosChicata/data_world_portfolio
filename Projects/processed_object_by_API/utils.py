'''
Purpose:
    define a utils methods to process data.
'''
import boto3


S3Client = boto3.client('s3')
rekog_client = boto3.client('rekognition')


def get_simpliflied_context(context):
    '''
    Purpose:
        simplified a context of s3 object lambda.
    Params:
        - context (dict) : context of s3 object lambda.
    return dict with data of context
    '''
    simple_context = dict()
    simple_context["object_url"] = context["getObjectContext"]["inputS3Url"]
    simple_context["route"] = context["getObjectContext"]["outputRoute"]
    simple_context["token"] = context["getObjectContext"]["outputToken"]
    simple_context["bucket"] = context["configuration"]["payload"]
    simple_context["key"] = context["userRequest"]["url"].split("/")[-1]
    return simple_context


def get_obj_from_s3(bucket, key):
    '''
    Purpose:
        get object from s3 bucket.
    Params:
        - bucket (string) : name of bucket.
        - key (string): name of object.
    Return Object
    '''
    return S3Client.get_object(
            Bucket=bucket,
            Key=key
        )


def extract_text_from_image(bucket=None, key=None, bytes=None):
    '''
    Purpose:
        extract text of image using rekognition service.
    Params:
        - bucket (string) : name of bucket.
        - key (string): name of object.
        - bytes (bytes) : image in bytes.
    return a response of service.
    '''
    imageFields = {}

    if bytes is not None:
        imageFields = {
            'Bytes': bytes
        }
    else:
        imageFields = {
            'S3Object': {
                'Bucket': bucket,
                'Name': key,
            }
        }

    return rekog_client.detect_text(Image=imageFields)


def to_user_from_s3ol(data, token, route):
    '''
    Purpose:
        return data to S3 object lambda.
    Params:
        - data (bytes): data will come back to user.
        - token (string): token to autenticate.
        - route (string): route to send data.
    return None
    '''
    S3Client.write_get_object_response(
            Body=data,
            RequestRoute=route,
            RequestToken=token,
        )
 
