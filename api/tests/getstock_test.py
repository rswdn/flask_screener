import flask
from flask import Flask, request
import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()


def test_ticker(client):
    data ={"ticker":"TSLA"}
    url = 'http://localhost:5000/getstock'
    response = client.post(url, data=data)
    assert response.status_code == 200

def test_wrong_ticker(client):
    data ={"ticker":"test"}
    url = 'http://localhost:5000/getstock'
    response = client.post(url, data=data)
    assert response.status_code == 404
