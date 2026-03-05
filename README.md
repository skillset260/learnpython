# learnpython

Simple CRUD APIs in Python using Flask.

## Setup

```powershell
cd .\learnpython
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install flask
```

## Run

```powershell
python app.py
```

Server starts on `http://127.0.0.1:5000`.

## API Endpoints

- `GET /` health check message
- `GET /items` list all items
- `GET /items/<id>` get one item
- `POST /items` create item
- `PUT /items/<id>` update item
- `DELETE /items/<id>` delete item

## Example Requests

Create item:

```powershell
curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"name":"Pen","price":10}'
```

List items:

```powershell
curl http://127.0.0.1:5000/items
```

Update item:

```powershell
curl -X PUT http://127.0.0.1:5000/items/1 -H "Content-Type: application/json" -d '{"name":"Blue Pen","price":12}'
```

Delete item:

```powershell
curl -X DELETE http://127.0.0.1:5000/items/1
```
