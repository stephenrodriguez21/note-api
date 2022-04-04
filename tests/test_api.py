import json
import pytest
from starlette.testclient import TestClient

from api.application import create_app



@pytest.fixture(scope="module")
def test_client():
    with TestClient(create_app()) as test_client:
        # testing
        yield test_client


def get_token(test_client):
    # Get token to call api endponts
    model = {
        "email": "author1@blog.com",
        "password": 123456
    }
    response = test_client.post("authenticate", json.dumps(model))
    return response.json()["token"]


def test_invalid_login(test_client):
    dicts = {
        "email": "invaliduser@blog.com",
        "password": 123456
    }
    response = test_client.post("authenticate", json.dumps(dicts))
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid login credentials"


def test_valid_login(test_client):
    dicts = {
        "email": "author1@blog.com",
        "password": 123456
    }
    response = test_client.post("authenticate", json.dumps(dicts))
    assert response.status_code == 200
    assert response.json()["token"] != ""


def test_load_all_blogs(test_client):
    response = test_client.get("blogs")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_and_delete_blog(test_client):
    token: str = get_token(test_client)
    dicts = {
        "name": "Testing Blog",
        "content": "This is the content part",
        "status": "created",
        "category_id": 1
    }

    # Test create blog endpoint
    response = test_client.post("blogs", json.dumps(dicts), headers={"x-token": token})
    assert response.status_code == 200
    assert response.json() != None
    assert response.json()["id"] > 0

    # Delete blog endpoint
    response = test_client.delete(f'blogs/{response.json()["id"]}', headers={"x-token": token})
    assert response.status_code == 200


def test_blog_not_found_error(test_client):
    token: str = get_token(test_client)

    # Test get blog endpoint when item does not exists
    response = test_client.get(f"blogs/{999999999999999999}", headers={"x-token": token})
    assert response.status_code == 404
    assert response.json()["detail"] == 'Item not found'


def test_when_edit_blog_with_invalid_token(test_client):
    token: str = 'some-invalid-token'

    # Test get blog endpoint when invalid token is sent
    response = test_client.get(f"blogs/{9}", headers={"x-token": token})
    assert response.status_code == 403





