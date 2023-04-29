from storages.backends.azure_storage import AzureStorage

import os

from dotenv import load_dotenv

load_dotenv()

# as per https://medium.com/@DawlysD/django-using-azure-blob-storage-to-handle-static-media-assets-from-scratch-90cbbc7d56be
class AzureMediaStorage(AzureStorage):
    account_name = os.environ.get(
        "AZURE_ACCOUNT_NAME"
    )  # Must be replaced by your <storage_account_name>
    account_key = os.environ.get(
        "AZURE_ACCOUNT_KEY"
    )  # Must be replaced by your <storage_account_key>
    azure_container = "media"
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = os.environ.get(
        "AZURE_ACCOUNT_NAME"
    )  # Must be replaced by your storage_account_name
    account_key = os.environ.get(
        "AZURE_ACCOUNT_KEY"
    )  # Must be replaced by your <storage_account_key>
    azure_container = "static"
    expiration_secs = None
