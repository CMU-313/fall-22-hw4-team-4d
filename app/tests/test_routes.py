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


