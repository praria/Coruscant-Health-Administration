from cryptography.fernet import Fernet
from django.conf import settings

# Generate a key only once using the following command and save it in settings.py
# python manage.py shell
# from cryptography.fernet import Fernet
# FILE_ENCRYPTION_KEY = print(Fernet.generate_key())

fernet = Fernet(settings.FILE_ENCRYPTION_KEY)

def encrypt_file(file_data):
    return fernet.encrypt(file_data)

def decrypt_file(file_data):
    return fernet.decrypt(file_data)
