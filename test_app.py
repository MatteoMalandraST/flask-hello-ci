import app, json

def test_root():
    c = app.app.test_client()
    r = c.get("/")
    assert r.status_code == 200
    assert json.loads(r.data)["msg"] == "hello devops!"