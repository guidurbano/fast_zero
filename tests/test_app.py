from http import HTTPStatus


def test_root_return_ok_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'johndoe',
            'email': 'johndoe@x.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'johndoe',
        'email': 'johndoe@x.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'johndoe',
                'email': 'johndoe@x.com',
                'id': 1,
            }
        ]
    }


def test_update_users(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'johnsmith',
            'email': 'johnsmith@x.com',
            'password': 'secret',
            'id': 1,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'johnsmith',
        'email': 'johnsmith@x.com',
        'id': 1,
    }
