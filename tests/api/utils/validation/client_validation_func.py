from http import HTTPStatus
from requests import Response


def _is_client_response_successful(response: Response) -> bool:
    return response.status_code == HTTPStatus.OK

def _is_client_response_forbidden(response: Response) -> bool:
    return response.status_code == HTTPStatus.FORBIDDEN

def _is_client_response_not_found(response: Response) -> bool:
    return response.status_code == HTTPStatus.NOT_FOUND

def _is_client_response_conflict(response: Response) -> bool:
    return response.status_code == HTTPStatus.CONFLICT