import os
import datetime
import unittest
from unittest.mock import patch

from dropbox import Dropbox
from dropbox.exceptions import AuthError
from dropbox.files import FileMetadata

from helpers.helper import (diff_files, Connection)

FILES_IN_DB = ['user.png','user_Ex6Ux0I.png',]
EXPECTED_RESULT = ['id:IXm8y2xS_d4AAAAAAAADew','id:IXm8y2xS_d4AAAAAAAADfw']
MOCK_FILES = [{'id': 'id:IXm8y2xS_d4AAAAAAAADZQ', 'name': 'user.png', 
            'path_display': '/home/joalbert/Documents/Remesas App/RemesasServer/media/identifications/images/user.png', 
            'client_modified': datetime.datetime(2021, 12, 16, 21, 52, 8), 
            'server_modified': datetime.datetime(2021, 12, 16, 21, 52, 9)}, 
            {'id': 'id:IXm8y2xS_d4AAAAAAAADdw', 'name': 'user_Ex6Ux0I.png', 
            'path_display': '/home/joalbert/Documents/Remesas App/RemesasServer/media/identifications/images/user_Ex6Ux0I.png', 
            'client_modified': datetime.datetime(2021, 12, 16, 21, 54, 40), 
            'server_modified': datetime.datetime(2021, 12, 16, 21, 54, 41)}, 
            {'id': 'id:IXm8y2xS_d4AAAAAAAADew', 'name': 'user_Pe9OmXf.png', 
            'path_display': '/home/joalbert/Documents/Remesas App/RemesasServer/media/identifications/images/user_Pe9OmXf.png', 
            'client_modified': datetime.datetime(2021, 12, 16, 21, 59, 24), 
            'server_modified': datetime.datetime(2021, 12, 16, 21, 59, 24)}, 
            {'id': 'id:IXm8y2xS_d4AAAAAAAADfw', 'name': 'user_VtIfC05.png', 
            'path_display': '/home/joalbert/Documents/Remesas App/RemesasServer/media/identifications/images/user_VtIfC05.png', 
            'client_modified': datetime.datetime(2021, 12, 16, 22, 2, 38), 
            'server_modified': datetime.datetime(2021, 12, 16, 22, 2, 38)}
            ]


MOCK_FILE_DATA = [FileMetadata(client_modified=datetime.datetime(2021, 12, 16, 21, 52, 8), 
                            content_hash='1bd7e5e07fb5dc77b5a406e67aa7eb97b9a7513e5bef3353f6bfe206f5d25fb4',  
                            id='id:IXm8y2xS_d4AAAAAAAADZQ', is_downloadable=True, name='user.png', 
                            path_display='/home/joalbert/Documents/Remesas App/RemesasServer/media/identifications/images/user.png', 
                            path_lower='/home/joalbert/documents/remesas app/remesasserver/media/identifications/images/user.png', 
                            rev='5d34a6f26c98b801c6701', server_modified=datetime.datetime(2021, 12, 16, 21, 52, 9), 
                            size=1669,), 
                FileMetadata(client_modified=datetime.datetime(2021, 12, 16, 21, 54, 40), 
                            content_hash='1bd7e5e07fb5dc77b5a406e67aa7eb97b9a7513e5bef3353f6bfe206f5d25fb4', 
                            id='id:IXm8y2xS_d4AAAAAAAADdw', is_downloadable=True, name='user_Ex6Ux0I.png', 
                            path_display='/home/joalbert/Documents/Remesas App/RemesasServer/media/identifications/images/user_Ex6Ux0I.png', 
                            path_lower='/home/joalbert/documents/remesas app/remesasserver/media/identifications/images/user_ex6ux0i.png', 
                            rev='5d34a7831e5b4801c6701', server_modified=datetime.datetime(2021, 12, 16, 21, 54, 41), size=1669), 
                FileMetadata(client_modified=datetime.datetime(2021, 12, 16, 21, 59, 24), 
                            content_hash='1bd7e5e07fb5dc77b5a406e67aa7eb97b9a7513e5bef3353f6bfe206f5d25fb4', 
                            id='id:IXm8y2xS_d4AAAAAAAADew', is_downloadable=True, name='user_Pe9OmXf.png',  
                            path_display='/home/joalbert/Documents/Remesas App/RemesasServer/media/identifications/images/user_Pe9OmXf.png', 
                            path_lower='/home/joalbert/documents/remesas app/remesasserver/media/identifications/images/user_pe9omxf.png', 
                            rev='5d34a891b4386801c6701', server_modified=datetime.datetime(2021, 12, 16, 21, 59, 24), size=1669,), 
                FileMetadata(client_modified=datetime.datetime(2021, 12, 16, 22, 2, 38), 
                            content_hash='1bd7e5e07fb5dc77b5a406e67aa7eb97b9a7513e5bef3353f6bfe206f5d25fb4', 
                            id='id:IXm8y2xS_d4AAAAAAAADfw', is_downloadable=True, name='user_VtIfC05.png',  
                            path_display='/home/joalbert/Documents/Remesas App/RemesasServer/media/identifications/images/user_VtIfC05.png', 
                            path_lower='/home/joalbert/documents/remesas app/remesasserver/media/identifications/images/user_vtifc05.png', 
                            rev='5d34a94ad0123801c6701', server_modified=datetime.datetime(2021, 12, 16, 22, 2, 38), 
                            size=1669,)
                ]       
                            

DELETED_FILES = ['id:IXm8y2xS_d4AAAAAAAADZQ', 'id:IXm8y2xS_d4AAAAAAAADdw']

class MockFolder:
    @property
    def entries(self):
        return MOCK_FILE_DATA


class TestHelper(unittest.TestCase):

    def test_connection_connect(self):
        token = "1234"
        con = Connection(token)
            
        with patch('helpers.helper.Dropbox') as Mock: 
            Mock.return_value = Dropbox(token)
            files = con._connect()
            self.assertIsInstance(files,Dropbox)
        
        with self.assertRaises(ConnectionError):
            with patch('helpers.helper.Dropbox') as Mock: 
                Mock.side_effect = ConnectionError
                files = con._connect()
                
        with self.assertRaises(AuthError):
            with patch('helpers.helper.Dropbox') as Mock: 
                Mock.side_effect = AuthError(1,"bad credentials")
                files = con._connect()
                
    def test_get_files(self):
        token = "1234"
        con = Connection(token)
            
        with patch('helpers.helper.Dropbox.files_list_folder') as Mock: 
            Mock.return_value = MockFolder()
            files = con.get_files()
            self.assertEqual(files[0],MOCK_FILES)
        
        with patch('helpers.helper.Dropbox.files_list_folder') as Mock: 
            Mock.side_effect = Exception("files not availables!")
            with self.assertRaises(Exception):
                files = con.get_files()

    def test_delete_files(self):
        token = "1234"
        con = Connection(token)
            
        with patch('helpers.helper.Dropbox.file_requests_delete') as Mock: 
            Mock.return_value = MockFolder()
            files = con.delete_files(DELETED_FILES)
            self.assertIsNone(files)
        
        with patch('helpers.helper.Dropbox.file_requests_delete') as Mock: 
            Mock.side_effect = Exception("Api error")
            with self.assertRaises(Exception):
                con.delete_files(DELETED_FILES)

    def test_diff_files(self): 
        result = diff_files(files_in_db=FILES_IN_DB,files_in_server=MOCK_FILES)
        self.assertEqual(result,EXPECTED_RESULT)


if __name__ == '__main__':
    unittest.main()
