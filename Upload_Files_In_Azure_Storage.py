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
def uploadToBlobStorage(file_path):
   blob_service_client = BlobServiceClient.from_connection_string(connection_string)

   #for filename in os.listdir(adresse):
   #  blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)


   data_paths = [i for i in (os.path.join(adresse, f) for f in os.listdir(adresse)) if os.path.isfile(i)]
   for i in data_paths: 
      blob_client = blob_service_client.get_blob_client(container=container_name, blob=i)
      with open(i,"rb") as data:
               blob_client.upload_blob(data)
      print(f"Fichier {i}. uploadé")
   
# calling a function to perform upload

adresse = input("Chemin du dossier à envoyer : ")

uploadToBlobStorage(adresse)
