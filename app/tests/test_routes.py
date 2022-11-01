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
    


def test_predict_route_invalid():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    
    #missing inputs
    url = '/predict?age=18&absences=19&health=3&G3=10&Dalc=3'
    response = client.get(url)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url2 = '/predict?age=18'
    response = client.get(url2)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url3 = '/predict'
    response = client.get(url3)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    #invalid inputs
    url4 = '/predict?age=14&absences=19&health=3&G3=1&Dalc=3&activities=yes'
    response = client.get(url4)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url5 = '/predict?age=23&absences=19&health=3&G3=1&Dalc=3&activities=yes'
    response = client.get(url5)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url6 = '/predict?age=18&absences=94&health=3&G3=1&Dalc=3&activities=yes'
    response = client.get(url6)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url7 = '/predict?age=18&absences=19&health=0&G3=1&Dalc=3&activities=yes'
    response = client.get(url7)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url8 = '/predict?age=18&absences=19&health=6&G3=1&Dalc=3&activities=yes'
    response = client.get(url8)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url9 = '/predict?age=18&absences=19&health=3&G3=21&Dalc=3&activities=yes'
    response = client.get(url9)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url10 = '/predict?age=18&absences=19&health=3&G3=1&Dalc=0&activities=yes'
    response = client.get(url10)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url11 = '/predict?age=18&absences=19&health=3&G3=1&Dalc=6&activities=yes'
    response = client.get(url11)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url12 = '/predict?age=18&absences=19&health=3&G3=1&Dalc=3&activities=bad'
    response = client.get(url12)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url13 = '/predict?age=bad&absences=19&health=3&G3=1&Dalc=3&activities=yes'
    response = client.get(url13)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url14 = '/predict?age=18&absences=bad&health=3&G3=1&Dalc=3&activities=yes'
    response = client.get(url14)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url15 = '/predict?age=18&absences=19&health=bad&G3=1&Dalc=3&activities=yes'
    response = client.get(url15)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url16 = '/predict?age=18&absences=19&health=3&G3=bad&Dalc=3&activities=yes'
    response = client.get(url16)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'

    url17 = '/predict?age=18&absences=19&health=3&G3=1&Dalc=bad&activities=yes'
    response = client.get(url17)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>400 Bad Request</title>\n<h1>400 Bad Request</h1>\n<p>Invalid input.</p>\n'



