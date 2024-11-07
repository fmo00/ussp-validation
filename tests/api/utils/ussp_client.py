from api.utils.client import UTMClientConfig
from requests import Request

class UsspClient(UTMClientConfig):
    def __init__(self, base_url):
        super().__init__(self) 
        self.base_url = base_url

    def request_put_oir(self):
        req = Request('GET', self.base_url, data={}, headers={})
        prep_req = self.session.prepare_request(req)
        return self.session.send(prep_req)
