from api_utils import Calls
from api_utils import Config
from unittest import TestCase
import httplib

# defining TestClass class using inheritance from TestCase class od module
class TestClass(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calls = Calls()
        cls.config = Config()


    def test_create_folder_positive(self):
        folder_name = self.calls.gen_random_name()
        resp = self.calls.create_folder(folder_name)
        assert resp.http_code == httplib.CREATED # or 201
        self.calls.delete_folder(folder_name)

    def test_delete_folder(self):
        folder_name = self.calls.gen_random_name()
        resp = self.calls.create_folder(folder_name)
        assert resp.http_code == httplib.CREATED # or 201
        resp = self.calls.delete_folder(folder_name)
        assert resp.http_code == httplib.OK # or 200


    def test_create_folder_incorrect_credentials(self):
        folder_name = self.calls.gen_random_name()
        resp = self.calls.create_folder(folder_name, password = 'asdas')
        assert resp.http_code == httplib.UNAUTHORIZED
        assert resp.json_body['inputErrors']['credentials'][0]['code'] == 'INVALID_CREDENTIALS'
        assert resp.json_body['inputErrors']['credentials'][0]['msg'] == 'This request is unauthenticated. ' \
                                                                         'Please provide credentials and try again.'

    def test_delete_non_existing_folder(self):
        folder_name = self.calls.gen_random_name()
        resp = self.calls.delete_folder(folder_name)
        assert self.http_code == httplib.NOT_FOUND
        assert resp.json_body['errorMessage'] == 'Item does not exist'

    #demanding wrong content_type from the server
    def test_delete_folder_wrong_accept_header(self):
        folder_name = self.calls.gen_random_name()
        resp = self.calls.delete_folder(folder_name, accept = 'application/xml')
        assert resp.http_code == httplib.NOT_ACCEPTABLE #or 406
        assert resp.json_body['errorMessage'] == 'Not Acceptablet'


    def test_method_not_allowed(self):
        #resp = self.calls.delete_folder(self.calls.gen_random_name(), method='UPDATE')
        folder_name = self.calls.gen_random_name()
        resp = self.calls.delete_folder(folder_name)
        assert resp.http_code == httplib.METHOD_NOT_ALLOWED #or 405
        assert resp.json_body['errorMessage'] == 'Method Not Allowed'


    def test_wrong_content_type(self):
        resp = self.calls.create_folder(self.calls.gen_random_name(), content_type='application/xml')
        assert resp.http_code == httplib.UNSUPPORTED_MEDIA_TYPE
        assert resp.json_body['errorMessage'] == 'Unsupported Media Type'


    def test_create_and_delete_100_folders_in_a_row(self):
        folder_name = self.calls.gen_random_name()
        for i in range(100):
            resp = self.calls.create_folder(folder_name + str(i))
            assert resp.http_code == httplib.CREATED
            assert resp.json_body == self.calls.no_json
        for i in range(100):
            resp = self.calls.delete_folder(folder_name + str(i))
            assert resp.http_code == httplib.OK
            assert resp.json_body == self.calls.no_json


    def test_perms(self):
        folder_name = self.calls.gen_random_name()
        self.calls.create_folder(folder_name)
        resp = self.calls.set_perms(folder_name, username=self.config.puser, test_path='%s/%s' % (self.config.test_path, folder_name))
        assert resp.http_code == httplib.CREATED





    # @classmethod
    # def tearDown(cls):