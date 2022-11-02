import boto3

#Initialize interfaces
s3Client = boto3.client('s3')
s3Resource = boto3.resource('s3')

#Create byte string to send to our bucket
putMessage = b"Hi! I came from boto3!"

#put_object
response = s3Client.put_object(
    Body = putMessage,
    Bucket = 'das-demos-flo',
    Key = 'boto3put.txt'
)

print(response)