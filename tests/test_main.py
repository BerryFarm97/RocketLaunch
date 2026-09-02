import httpx
import pytest
import main

URL_TIMEOUT = 10

fake_json = {
    "count": 1,
    "next": None,
    "previous": None,
    "results": [{"id": "test-launch", "name": "Test Launch"}],
}


class FakeResponse:
    def __init__(self, fake_json, status_error=None):
        self.fake_json = fake_json
        self.status_error = status_error

    def raise_for_status(self):
        if self.status_error is not None:
            raise self.status_error
        else:
            return None

    def json(self):
        return self.fake_json


def test_get_api_data_returns_valid_envelope(monkeypatch):
    params = {
        "limit": 1,
    }

    def mock_get(url, params, timeout):
        return FakeResponse(fake_json)

    monkeypatch.setattr(main.httpx, "get", mock_get)

    response = main.get_api_data(
        "www.BerryFarmsWonderland.com/", params=params, timeout=URL_TIMEOUT
    )

    assert response == fake_json
