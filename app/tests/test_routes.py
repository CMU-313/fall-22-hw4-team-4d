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
    url1 = '/predict?health=5&absences=2&Medu=4&Fedu=4&Dalc=1'
    response1 = client.get(url1)
    assert response1.status_code == 200
    assert response1.get_data() == b'0\n'

    # Test 2
    url2 = '/predict?health=5&absences=2&Medu=4&Fedu=4&Dalc=1'
    response2 = client.get(url2)
    assert response2.status_code == 200
    assert response2.get_data() == b'0\n'

    # Test 3
    url3 = '/predict?health=5&absences=2&Medu=4&Fedu=4&Dalc=1'
    response3 = client.get(url3)
    assert response3.status_code == 200
    assert response3.get_data() == b'0\n'

    # Test 4
    url4 = '/predict?health=5&absences=2&Medu=4&Fedu=4&Dalc=1'
    response4 = client.get(url4)
    assert response4.status_code == 200
    assert response4.get_data() == b'0\n'


    # Test 5
    url5 = '/predict?health=5&absences=2&Medu=4&Fedu=4&Dalc=1'
    response5 = client.get(url5)
    assert response5.status_code == 200
    assert response5.get_data() == b'0\n'
    


def test_predict_route_invalid():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    
    #missing inputs
    url = '/predict?health=5&absences=2&Medu=4&Fedu=4'
    response = client.get(url)
    assert response.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url2 = '/predict?age=18'
    response2 = client.get(url2)
    assert response2.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url3 = '/predict'
    response3 = client.get(url3)
    assert response3.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    #invalid inputs
    url4 = '/predict?absences=19&health=3&Dalc=3'
    response4 = client.get(url4)
    assert response4.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url5 = '/predict?absences=19&health=3&G3=1&Dalc=3'
    response5 = client.get(url5)
    assert response5.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url6 = '/predict?health=5&absences=2000&Medu=4&Fedu=4&Dalc=1'
    response6 = client.get(url6)
    assert response6.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url7 = '/predict?health=5&absences=-5&Medu=4&Fedu=4&Dalc=1'
    response7 = client.get(url7)
    assert response7.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url8 = '/predict?health=-5&absences=5&Medu=4&Fedu=4&Dalc=1'
    response8 = client.get(url8)
    assert response8.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url9 = '/predict?health=300&absences=5&Medu=4&Fedu=4&Dalc=1'
    response9 = client.get(url9)
    assert response9.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url10 = '/predict?health=5&absences=2&Medu=20&Fedu=4&Dalc=1'
    response10 = client.get(url10)
    assert response10.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url11 = '/predict?health=5&absences=2&Medu=-4&Fedu=4&Dalc=1'
    response11 = client.get(url11)
    assert response11.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url12 = '/predict?health=5&absences=2&Medu=20&Fedu=4&Dalc=1'
    response12 = client.get(url12)
    assert response12.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url13 = '/predict?health=5&absences=2&Medu=2&Fedu=-4&Dalc=1'
    response13 = client.get(url13)
    assert response13.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url14 = '/predict?health=5&absences=2&Medu=4&Fedu=20&Dalc=1'
    response14 = client.get(url14)
    assert response14.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url15 = '/predict?health=5&absences=2&Medu=4&Fedu=4&Dalc=-1'
    response15 = client.get(url15)
    assert response15.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url16 = '/predict?health=5&absences=2&Medu=4&Fedu=4&Dalc=21'
    response16 = client.get(url16)
    assert response16.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'

    url17 = '/predict?health=health&absences=2&Medu=4&Fedu=4&Dalc=1'
    response17 = client.get(url17)
    assert response17.get_data() == b'<!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'