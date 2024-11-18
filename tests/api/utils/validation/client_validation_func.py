from http import HTTPStatus
from requests import Response


def _is_client_response_successful(response: Response) -> bool:
    return response.status_code == HTTPStatus.OK


def _is_client_forbidden(response: Response) -> bool:
    return response.status_code == HTTPStatus.FORBIDDEN
