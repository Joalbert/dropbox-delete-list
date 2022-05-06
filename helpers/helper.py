import sys
import csv
from typing import List, Dict, Iterable, Tuple, Type, Any

from dropbox import Dropbox
from dropbox.exceptions import AuthError
from dropbox.files import FileMetadata

def diff_files(*, files_in_db:Iterable[str], files_in_server:Iterable[Dict[str, str]], field_output: str="id")->List[str]:
    ''' Check difference between existant and files_in_db lists and elements not in files_in_db will be returned'''
    diff:List[str] = list()
    for file in files_in_server:
        if not (file["name"] in files_in_db):
            diff.append(file[field_output])
    return diff 

def format_csv(path_csv:str)->List[str]:
    """With first row of csv files which has a path get filename and return a list of filenames"""
    filenames:List[str] = []
    with open(path_csv) as f:
        spamreader = csv.reader(f, delimiter=' ', quotechar=',')
        for index, row in enumerate(spamreader):
            if index==0:
                continue
            name = str(row).split(",")[0].split("/")[-1]
            filenames.append(name)
    return filenames

class Connection:
    """Connection to Dropbox Server"""
    def __init__(self, token:str)->None:
        self.token = token
    
    def _connect(self)-> Type[Dropbox]: 
        """Connect to dropbox server"""
        try:
            dbx = Dropbox(self.token) 
        except ConnectionError:
            print("Connection Trouble. Please, check your internet connection!\n", file=sys.stderr)
            raise 
        except AuthError as e:
            print("Authentication Error. Please, check if token is still valid!\n", file=sys.stderr)
            raise 
        else:
            return dbx
        
    def get_files(self, *, path:str="")->Tuple[List[Dict[str, Any]], List[Any]]:
        """Return a tuples with a list of files in a given Dropbox folder path for first element, and list of directory for 
        second element."""
        try:
            dbx = self._connect()
            folder = dbx.files_list_folder(path)
        except (Exception, ConnectionError) as e:
            print(f'Error getting list of files from Dropbox: {str(e)} \n',file=sys.stderr)
            raise

        else:
            files = folder.entries
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
                    directory_list.append(file.name)
            return (files_list, directory_list)
    
    def delete_files(self, file_id:Iterable[str])->None:
        """Delete files/directory from a iterable"""
        try:
            dbx = self._connect()
            for file in file_id:
                dbx.files_delete(path=file)
                print(f'File: {file} was successfully deleted!\n',file=sys.stdout)                
        except Exception as e:
            print(f'Error deleting the list of files from Dropbox: {str(e)} \n',file=sys.stderr)
            raise
            
            

if __name__ == "__main__":
    print("it would not support terminal mode!")