from azure.storage.blob import BlobServiceClient
import os
import time

account_name = os.getenv('STORAGE_ACCOUNT_NAME')
account_key = os.getenv('STORAGE_ACCOUNT_KEY')

connection_string = input('Entrez la clé de connexion : ')
time.sleep(3)
print("Presque fini ! ")

container_name = input('Entrez le nom du conteneur : ')
time.sleep(3)
print("Enregistré ! 👀")
def uploadToBlobStorage(file_path,file_name):
   blob_service_client = BlobServiceClient.from_connection_string(connection_string)
   blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
   with open(file_path,"rb") as data:
      blob_client.upload_blob(data)
      print(f"Fichier {file_name}. uploadé")
# calling a function to perform upload
adresse = input("Chemin du fichier à envoyer : ")
name_file = input("Nom du fichier à mettre : ")

uploadToBlobStorage(adresse,name_file)