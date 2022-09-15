from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "docs": "api documentation at /docs or /redoc",
        "editor": "newsletter editor at /editor",
    }
