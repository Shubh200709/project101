import os, dropbox
from dropbox.files import WriteMode

class TransferData:
    def _init_(self, access_token):
        self.access_token = access_token

    def upload(self, files_from, files_to):
        dbx = dropbox.Dropbox(self.access_token)
        for roots, dirs, files in os.walk(files_from):
            for filename in files:
                local_path = os.path.join(roots, filename)
                relative_path = os.path.relpath(local_path, files_from)
                dropbox_path = os.path.join(files_to,relative_path)

                with open(local_path,'rb') as f:
                    dbx.files_upload(f.open(), dropbox_path, mode = WriteMode("overwrite"))

def main():
    access_token = "riFu6Ybhc9AAAAAAAAAAHWkfE9AiGyD6n4254tOxesw7ShRjGjFhrjhRVa3NX3mx"
    transferData = TransferData(access_token)
    
    files_from = input("Enter the pathway of the files")
    files_to = input("Enter the pathway to send the files")
    transferData.upload(files_from,files_to)
    print("files transfered successfully!!")

main()