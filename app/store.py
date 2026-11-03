import itertools


class TodoStore:
    """In-memory todo storage."""

    def __init__(self):
        self._todos = {}
        self._ids = itertools.count(1)

    def list(self):
        return list(self._todos.values())

    def get(self, todo_id):
        return self._todos.get(todo_id)

    def add(self, title, due=None):
        todo = {"id": next(self._ids), "title": title, "done": False, "due": due}
        self._todos[todo["id"]] = todo
        return todo

    def update(self, todo_id, **fields):
        todo = self._todos[todo_id]
        todo.update(fields)
        return todo

    def delete(self, todo_id):
        return self._todos.pop(todo_id, None)

    def search(self, text):
        text = text.lower()
        return [t for t in self._todos.values() if text in t["title"].lower()]
