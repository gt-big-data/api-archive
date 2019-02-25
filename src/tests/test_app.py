import os
import tempfile
import pytest
from flask import Flask
from flask import app

@pytest.fixture
def client():
    client = app
    yield client

def test_ping(client):
    p = client.get('/aman')
    assert 'pong' in p
