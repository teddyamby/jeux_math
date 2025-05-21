from main import app
import pytest

def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Jeu de Calcul Mathématique" in response.data

def test_get_question_route():
    client = app.test_client()
    response = client.get('/get_question')
    assert response.status_code == 200
    assert b"question" in response.data

def test_check_answer_route():
    client = app.test_client()
    response = client.post('/check_answer', json={"id": 1, "answer": 5})
    assert response.status_code == 200
    assert b"correct" in response.data