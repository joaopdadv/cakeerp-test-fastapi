from urllib import response
from tests.config import *

def test_status():
    response=client.get("/status")
    data=response.json()
    assert response.status_code==200
    assert data["message"]=="ok"