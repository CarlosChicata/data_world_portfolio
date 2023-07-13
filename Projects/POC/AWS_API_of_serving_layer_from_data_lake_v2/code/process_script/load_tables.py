import argparse


import boto3


# define args in script 
argParser = argparse.ArgumentParser()
argParser.add_argument("--bucket-origin", 
        help="the name of origin bucket", required=True)
argParser.add_argument("--bucket-destiny", 
        help="the name of destiny bucket", required=True)

# get params
### i need unknown to handle unrecognize args.
args, unknown = argParser.parse_known_args()



s3 = boto3.resource("s3")
bucket = s3.Bucket(args.bucket_origin)

for obj in bucket.objects.all():
    source_filename = (obj.key).split("/")[-1]
    folder_name = source_filename.split(".")[0]
    folder_name = folder_name.replace("_","-")

    copy_source = {
        "Bucket": args.bucket_origin,
        "Key": obj.key
    }
    list_target = [folder_name, obj.key]
    list_target = [ x for x in list_target if x is not None ]
    target_filename = "/".join(list_target)
    s3.meta.client.copy(copy_source, args.bucket_destiny, target_filename)
    
