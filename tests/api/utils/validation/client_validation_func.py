from http import HTTPStatus
from requests import Response


def _is_client_response_successful(response: Response) -> bool:
    return response.status_code == HTTPStatus.OK
