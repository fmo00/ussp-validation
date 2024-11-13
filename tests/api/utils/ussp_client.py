from api.utils.client import UTMClientConfig
from requests import Request


class UsspClient(UTMClientConfig):
    def __init__(self, session, base_url):
        super().__init__()
        self.base_url = base_url
        self.session = session

    def request_put_oir(self, oir_id, request_body):
        req = Request("PUT", self.base_url + oir_id, data=request_body, headers={})
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err

    def request_get_oir(self, oir_id):
        url = self.base_url + f"/operational_intents/${oir_id}"
        req = Request("GET", url, {}, {})
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err

    def request_put_flight_plans(self, flight_plan_id):
        url = self.base_url + f"/flight_plans/${flight_plan_id}"
        body = {}

        req = Request("PUT", url, data=body, headers={})
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)

        except Exception as err:
            raise err
