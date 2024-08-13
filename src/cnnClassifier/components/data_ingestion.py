import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
import boto3
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        self.s3_client = boto3.client('s3')


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            bucket_name, key = self._parse_s3_url(self.config.source_URL)
            self.s3_client.download_file(
                    Bucket=bucket_name,
                    Key=key,
                    Filename=self.config.local_data_file
                )
            logger.info(f"{self.config.local_data_file} download! ")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  


    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
    def _parse_s3_url(self, url):
        """Helper function to extract bucket name and key from the S3 URL."""
        if url.startswith("s3://"):
            url = url[len("s3://"):]
        bucket_name, key = url.split('/', 1)
        return bucket_name, key