def test_health(client):
    assert client.get("/health").json == {"status": "ok"}


def test_create_and_list(client):
    resp = client.post("/todos", json={"title": "buy milk"})
    assert resp.status_code == 201
    assert client.get("/todos").json == [{"id": 1, "title": "buy milk", "done": False}]


def test_title_required(client):
    assert client.post("/todos", json={"title": "  "}).status_code == 400


def test_complete(client):
    client.post("/todos", json={"title": "write tests"})
    assert client.patch("/todos/1", json={"done": True}).json["done"] is True


def test_delete(client):
    client.post("/todos", json={"title": "temp"})
    assert client.delete("/todos/1").status_code == 204
    assert client.get("/todos").json == []


def test_missing_todo_is_404(client):
    assert client.get("/todos/99").status_code == 404
    assert client.patch("/todos/99", json={"done": True}).status_code == 404
    assert client.delete("/todos/99").status_code == 404
