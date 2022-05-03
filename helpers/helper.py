import sys
import csv

from dropbox import Dropbox
from dropbox.exceptions import AuthError
from dropbox.files import FileMetadata

def diff_files(*, files_in_db:"list[dict]", files_in_server:"list[str]", field_output: str="id")->"list[str]":
    ''' Check difference between existant and files_in_db lists and elements not in files_in_db will be returned'''
    diff = list()
    for file in files_in_server:
        if not (file["name"] in files_in_db):
            diff.append(file[field_output])
    return diff 

def format_csv(path_csv:str)->"list[str]":
    """With first row of csv files which has a path get filename and return a list of filenames"""
    filenames = []
    with open(path_csv) as f:
        spamreader = csv.reader(f, delimiter=' ', quotechar=',')
        for row in spamreader:
            name = str(row).split(",")[0].split("/")[-1]
            filenames.append(name)
    return filenames

class Connection:
    """Connection to Dropbox Server"""
    def __init__(self, token:str)->None:
        self.token = token
    
    def _connect(self)->None:
        """Connect to dropbox server"""
        try:
            dbx = Dropbox(self.token) 
        except ConnectionError:
            sys.stderr.write("Connection Trouble. Please, check your internet connection!\n")
            raise 
        except AuthError as e:
            sys.stderr.write("Authentication Error. Please, check if token is still valid!\n")
            raise 
        else:
            return dbx
        
    def get_files(self, *, path:str="")->tuple:
        """Return a tuples with a list of files in a given Dropbox folder path for first element, and list of directory for 
        second element."""
        try:
            dbx = self._connect()
            folder = dbx.files_list_folder(path)
            files = folder.entries
        except Exception as e:
            sys.stderr.write(f'Error getting list of files from Dropbox: {str(e)} \n')
            raise

        else:
            files_list, directory_list = [], []
            for file in files:
                if isinstance(file, FileMetadata):
                    metadata = {
                        'id': file.id,
                        'name': file.name,
                        'path_display': file.path_display,
                        'client_modified': file.client_modified,
                        'server_modified': file.server_modified
                    }
                    files_list.append(metadata)
                else:
                    directory_list.append(file)
            return (files_list, directory_list)
    
    def delete_files(self, file_id:"list[str]")->None:
        """Delete file_id list"""
        try:
            dbx = self._connect()
            dbx.file_requests_delete(file_id)
        except Exception as e:
            sys.stderr.write(f'Error deleting the list of files from Dropbox: {str(e)} \n' )
            raise
        else:
            sys.stdout.write(f'File: {file_id} was successfully deleted!\n')

if __name__ == "__main__":
    print("it would not support terminal mode!")