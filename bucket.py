import boto3
from django.conf import settings
from requests import delete


class Bucket:
    """ CDN BUCKET manager
    init method creates connection.

    NOTE:
        none of this methods are async.use public interface in tasks.py modules intead.
    
    
    
    """


    def __init__(self) -> None:
        session=boto3.Session()
        self.conn=session.client(


            service_name=settings.AWS_SERVICE_NAME,
            aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,    
            
        )
    def get_objects(self):
        result=self.conn.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        if result['KeyCount']:
            return result['Contents']

        else:            
            return None
        
    def delete_object(self,key):
        self.conn.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME,Key=key)
        return True
        
        
    def download_file_obj(self,key):
        with open(settings.AWS_LOCAL_STORAGE+key,'wb') as f:
            self.conn.download_fileobj(settings.AWS_STORAGE_BUCKET_NAME,key,f)

        return True

    def upload_file_obj(self,key):
        with open(key,'rb')as f:
            self.conn.upload_file(f,settings.AWS_STORAGE_BUCKET_NAME,Key='None')

        return True

    
bucket=Bucket()       
        
        
        
        
        
        
        
        
        
        
        
        