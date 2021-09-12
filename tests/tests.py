from starlette.testclient import TestClient

from ships import app

client = TestClient(app)

def test_ships_status_code():
    response = client.get("/")
    assert response.status_code == 200
