from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return JSONResponse(content={"message": "Hello,  World"}, status_code=200)


@app.get("/profiles/")
def get_query_parameter(start: int = 0, limit: int = 0):

    response = {"message": f"start: {start} limit: {limit}"}

    return JSONResponse(
        content=response,
        status_code=200,
    )


@app.get("/profiles/{name}")
def get_path_parameter(name: str):

    response = {"message": f"My name is: {name}"}

    return JSONResponse(
        content=response,
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

    response = {"status": "ok", "data": dict_books}

    return JSONResponse(content=response, status_code=200)


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

    book_filter = {}
    for book in dict_books:
        if book["book_id"] == book_id:
            book_filter = book

    response = {"status": "ok", "data": book_filter}

    return JSONResponse(content=response, status_code=200)


class createBookPayload(BaseModel):
    id: str
    name: str
    page: int


@app.post("/books")
def create_books(req_body: createBookPayload):
    req_body_dict = req_body.dict()

    id = req_body_dict["id"]
    name = req_body_dict["name"]
    page = req_body_dict["page"]

    print("[ Log ] name", id)
    print("[ Log ] name", name)
    print("[ Log ] page", page)

    book = {
        "id": id,
        "name": name,
        "page": page,
    }

    response = {"status": "ok", "data": book}

    return JSONResponse(content=response, status_code=201)


class updateBookPayload(BaseModel):
    name: str = ""
    page: int = 0


@app.patch("/books/{book_id}")
def update_book_by_id(req_body: updateBookPayload, book_id: str):
    req_body_dict = req_body.dict()

    name = req_body_dict["name"]
    page = req_body_dict["page"]

    print("[ Log ] books_id", book_id)
    print("[ Log ] name", name)
    print("[ Log ] page", page)

    update_message = f"Update book id {book_id} is complete !! "
    response = {"status": "ok", "data": update_message}
    return JSONResponse(content=response, status_code=200)


@app.delete("/books/{book_id}")
def delete_book_by_id(book_id: str):

    print("[ Log ] Delete Book Id: ", book_id)

    delete_message = f"Delete book id {book_id} is complete !! "
    response = {"status": "ok", "data": delete_message}
    return JSONResponse(content=response, status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)
