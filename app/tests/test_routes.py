from flask import Flask

from app.handlers.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'

def test_predict_route_valid():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()

    # Test 1
    url1 = '/predict?age=30&absences=92&health=5&G3=20&Dalc=5&activities=yes'
    response1 = client.get(url1)
    assert response1.status_code == 200
    assert response1.get_data() == b'0\n'

    # Test 2
    url2 = '/predict?age=17&absences=1&health=5&G3=20&Dalc=4&activities=yes'
    response2 = client.get(url2)
    assert response2.status_code == 200
    assert response2.get_data() == b'0\n'

    # Test 3
    url3 = '/predict?age=17&absences=3&health=5&G3=20&Dalc=1&activities=yes'
    response3 = client.get(url3)
    assert response3.status_code == 200
    assert response3.get_data() == b'1\n'

    # Test 4
    url4 = '/predict?age=17&absences=40&health=4&G3=15&Dalc=5&activities=yes'
    response4 = client.get(url4)
    assert response4.status_code == 200
    assert response4.get_data() == b'0\n'


    # Test 5
    url5 = '/predict?age=20&absences=15&health=5&G3=20&Dalc=1&activities=yes'
    response5 = client.get(url5)
    assert response5.status_code == 200
    assert response5.get_data() == b'1\n'
    
