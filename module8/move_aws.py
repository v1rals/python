import boto3


def move_files(name):
    s3 = boto3.resource('s3')
    src_bucket = input("input source bucket name")
    try:
        bucket = s3.Bucket(src_bucket)
        dest_bucket = s3.create_bucket(Bucket=name)
        for obj in bucket.objects.filter():
            dest_key = obj.key
            s3.Object(dest_bucket.name, dest_key).copy_from(CopySource={'Bucket': obj.bucket_name, 'Key': obj.key})
    except Exception:
        print("something's wrong, please check input values")
