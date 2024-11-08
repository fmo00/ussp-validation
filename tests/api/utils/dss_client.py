from api.utils.client import UTMClientConfig
from requests import Request

class DssClient(UTMClientConfig):
    def __init__(self, session, base_url):
        super().__init__() 
        self.base_url = base_url
        self.session = session

    def request_get_oir_query(self, request_body):
        url = self.base_url + f'/operational_intent_references/query'
       
        req = Request('GET', url, request_body, headers={})
        prepped_req = self.session.prepare_request(req)
        return self.session.send(prepped_req)
    