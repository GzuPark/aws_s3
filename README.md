# S3Resource
Upload and Download an object via AWS S3 service.

## Requirements
```
boto3
```

## How to use
This code handle only object, not a file. Also, please set the `aws_access_key` and `aws_secret_access_key` if you have not set up yet. 
1. __s3_key__: _String_, The access key for AWS account
2. __s3_secret__: _String_, The secret key for AWS account
3. __s3_bucket__: _String_, The bucket name on AWS S3 service
4. __filename__: _String_, a file name with extension if you upload an object at the bucket
5. __obj__: _Object_, an object, already load from a file

```python
# example: DO NOT hard coding them on code lines
S3_KEY = 'S3_KEY'
S3_SECRET = 'S3_SECRET_ACCESS_KEY'
S3_BUCKET = 'S3_BUCKET_NAME'
```

### Upload
```python
from aws_s3.connection import S3Resource

resource = S3Resource(s3_key=S3_KEY, s3_secret=S3_SECRET)
resource.upload(s3_bucket=S3_BUCKET, filename='helloworld.jpg', data=image_object)
```

### Download
```python
from aws_s3.connection import S3Resource

resource = S3Resource(s3_key=S3_KEY, s3_secret=S3_SECRET)
result = resource.download(s3_bucket=S3_BUCKET, filename='helloworld.jpg')
```

## References
1. [User guide: AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
2. [boto3: Boto3 method parameters](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#method-parameters)
3. [boto3: Boto3 S3 put_object](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object)
4. [boto3: Boto3 S3 get_object](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_object)
5. [stackoverflow: write files directly to S3 using boto3](https://stackoverflow.com/questions/48491839/any-way-to-write-files-directly-to-s3-using-boto3)
6. [Upload files to S3, high-level and low-level](https://zindilis.com/docs/aws/s3/upload-file-with-boto3.html)
