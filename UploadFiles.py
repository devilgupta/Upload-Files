import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
        
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.Ah8hq5NqBhhP9zQBPitrIAXfUiJr-l93udLXzX7dhxss0ym_nEPY__yaLcID70-VZaOjAYl29_cXrvJBQHyHxJNyfifTpmvzkFnd10mdYzY9QQpsG99jnnXzsyeYSRq87mCkpm8'
    transferData=TransferData(access_token)

    file_from=input("Enter File Path to transfer:-")
    file_to=input("Enter full path to upload to dropbox:-")

    transferData.upload_file(file_from,file_to)
    print("File has been moved")

main()
