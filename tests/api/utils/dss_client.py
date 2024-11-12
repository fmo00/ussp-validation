from api.utils.client import UTMClientConfig
from requests import Request

class DssClient(UTMClientConfig):
    def __init__(self, session, base_url):
        super().__init__() 
        self.base_url = base_url
        self.session = session

    def request_get_oir_query(self, oir_id):
        url = self.base_url + f'/operational_intent_references/${oir_id}'
       
        req = Request('GET', url, {}, {})
        prepped_req = self.session.prepare_request(req)
        return self.session.send(prepped_req)
    