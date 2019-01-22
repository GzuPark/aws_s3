import os

import boto3


class S3Resource:
    """
    Upload and Downloading an object via AWS S3 service.
    """

    def __init__(self, s3_key, s3_secret):
        self.s3 = boto3.resource(
            's3',
            aws_access_key_id=s3_key,
            aws_secret_access_key=s3_secret,
        )

    def upload(self, s3_bucket, filename, obj):
        self.s3.Bucket(s3_bucket).put_object(
            Key=filename,
            Body=obj,
        )

    def download(self, s3_bucket, filename):
        response = self.s3.meta.client.get_object(
            Bucket=s3_bucket,
            Key=filename,
        )

        return response['Body'].read()
        