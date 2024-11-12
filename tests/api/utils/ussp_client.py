from api.utils.client import UTMClientConfig
from requests import Request
import uuid

class UsspClient(UTMClientConfig):
    def __init__(self, session, base_url):
        super().__init__() 
        self.base_url = base_url
        self.session = session

    def request_put_oir(self, oir_id, request_body):
        req = Request('PUT', self.base_url + oir_id, data=request_body, headers={})
        prepped_req = self.session.prepare_request(req)
        return self.session.send(prepped_req)
    
    def request_get_oir(self, oir_id):
        url = self.base_url + f'/operational_intents/${oir_id}'
        req = Request('GET', url, {},{})
        prepped_req = self.session.prepare_request(req)
        return self.session.send(prepped_req)
    