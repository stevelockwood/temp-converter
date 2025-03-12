import pytest

@pytest.fixture
def app():
    import main
    main.app.testing = True
    return main.app.test_client()


def test_index(app):
    r = app.get('/')
    assert r.status_code == 200

@pytest.mark.skip
def test_alwaysfails(app):
    r = app.get('/')
    assert True == False

def test_alwayssucceeds(app):
    r = app.get('/')
    assert True == True
