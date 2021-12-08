from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'mangost' # Must be replaced by your <storage_account_name>
    account_key = 'bWlIglAQuXEEsMvOvJ6KVOydcxTBlPgHWn7je2ZGopdQXzbrV4k89e+tYzNs33MUYaM4PZ6PXyAkwJNftuSvjg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

