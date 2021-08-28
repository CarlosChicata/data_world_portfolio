'''
Purpose:
    extract text from image to return data
'''
import json

from utils import get_simpliflied_context, to_user_from_s3ol, get_obj_from_s3, extract_text_from_image


def lambda_handler(event, context):
    easy_context = get_simpliflied_context(event)
    
    image = get_obj_from_s3(
            bucket=easy_context["bucket"],
            key=easy_context["key"]
        ).get("Body").read()

    response = extract_text_from_image(bytes=image)
    response =  [ line['DetectedText'] for line in response['TextDetections'] ]
    response = " ".join(response)
    
        
    to_user_from_s3ol(
            data=response,
            token=easy_context["token"],
            route=easy_context["route"]
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success operation!')
    }
