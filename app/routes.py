from flask import Blueprint, abort, jsonify, request

from app.store import TodoStore

bp = Blueprint("todos", __name__)
store = TodoStore()


def _get_or_404(todo_id):
    todo = store.get(todo_id)
    if todo is None:
        abort(404)
    return todo


@bp.get("/health")
def health():
    return {"status": "ok"}


@bp.get("/todos")
def list_todos():
    return jsonify(store.list())


@bp.post("/todos")
def create_todo():
    body = request.get_json(force=True)
    title = (body.get("title") or "").strip()
    if not title:
        return {"error": "title is required"}, 400
    return store.add(title, due=body.get("due")), 201


@bp.get("/todos/<int:todo_id>")
def get_todo(todo_id):
    return _get_or_404(todo_id)


@bp.patch("/todos/<int:todo_id>")
def update_todo(todo_id):
    _get_or_404(todo_id)
    body = request.get_json(force=True)
    fields = {k: body[k] for k in ("title", "done") if k in body}
    return store.update(todo_id, **fields)


@bp.delete("/todos/<int:todo_id>")
def delete_todo(todo_id):
    _get_or_404(todo_id)
    store.delete(todo_id)
    return "", 204


@bp.get("/todos.csv")
def export_csv():
    lines = ["id,title,done"] + [f'{t["id"]},{t["title"]},{t["done"]}' for t in store.list()]
    return "\n".join(lines), 200, {"Content-Type": "text/csv"}
