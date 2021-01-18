from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return JSONResponse(content={"message": "Hello,  World"}, status_code=200)


@app.get("/example/")
def get_query_parameter(start: int, limit: int):
    return JSONResponse(
        content={"message": f"start: {start} limit: {limit}"},
        status_code=200,
    )


@app.get("/profile/{name}")
def get_path_parameter(name: str):
    return JSONResponse(
        content={"message": f"My name is: {name}"},
        status_code=200,
    )


@app.get("/books")
def get_books():
    dict_books = [
        {
            "book_id": 1,
            "book_name": "Harry Potter and Philosopher's Stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "Harry Potter and the Chamber of Secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "Harry Potter and the Prisoner of Azkaban",
            "page": 251,
        },
    ]

    return JSONResponse(content={"status": "ok", "data": dict_books}, status_code=200)


@app.get("/books/{book_id}")
def get_books_by_id(book_id: int):
    dict_books = [
        {
            "book_id": 1,
            "book_name": "Harry Potter and Philosopher's Stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "Harry Potter and the Chamber of Secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "Harry Potter and the Prisoner of Azkaban",
            "page": 251,
        },
    ]

    book_filter = list(filter(lambda book: book["book_id"] == book_id, dict_books))
    result = filter_book[0] if len(filter_book) > 0 else []
    return JSONResponse(content={"status": "ok", "data": result}, status_code=200)


class Books(BaseModel):
    name: str
    page: int


@app.post("/books")
def create_books(req_body: Books):
    req_body_dict = req_body.dict()

    name = req_body_dict["name"]
    page = req_body_dict["page"]

    print("[ Log ] name", name)
    print("[ Log ] page", page)

    mock_response = {
        "_id": 4,
        "name": name,
        "page": page,
    }
    return JSONResponse(
        content={"status": "ok", "data": mock_response}, status_code=201
    )


class updateBooks(BaseModel):
    book_id: str
    name: str = ""
    page: int = 0


@app.patch("/books")
def update_book_by_id(req_body: updateBooks):
    req_body_dict = req_body.dict()
    books_id = req_body_dict["book_id"]

    print("[ Log ] books_id", books_id)

    mock_response = f"Update book id {books_id} is complete !! "
    return JSONResponse(
        content={"status": "ok", "data": mock_response}, status_code=200
    )


@app.delete("/books/{book_id}")
def delete_book_by_id(book_id: int):

    print("[ Log ] Delete Book Id: ", book_id)

    mock_response = f"Delete book id {book_id} is complete !! "
    return JSONResponse(
        content={"status": "ok", "data": mock_response}, status_code=200
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)
