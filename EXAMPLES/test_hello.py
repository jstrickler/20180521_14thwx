'''
Created on May 23, 2018

@author: jstrick
'''
import pytest

from hello_world import app

@pytest.fixture
def client():
    test_client = app.test_client()
    return test_client
    
def test_nothing(client):
    assert True
    
def test_root_has_hello(client):
    response = client.get('/')
    assert "Hello" in response.data
    
def test_barf_has_ugly(client):
    response = client.get('/barf')
    assert "ugly" in response.data

def test_potus_26_is_tr(client):
    response = client.get('/potus/26')
    assert "Theodore Roosevelt" in response.data
    


