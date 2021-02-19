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
def get_query_parameter(start: int = 0, limit: int = 0):
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
    books = [
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

    return JSONResponse(content={"status": "ok", "data": books}, status_code=200)


@app.get("/books/{book_id}")
def get_books_by_id(book_id: int):
    book = {
        "book_id": 1,
        "book_name": "Harry Potter and Philosopher's Stone",
        "page": 223,
    }

    response = {"status": "ok", "data": book}

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

    book = {
        "id": id,
        "name": name,
        "page": page,
    }

    response = {"status": "ok", "data": book}

    return JSONResponse(content=response, status_code=201)


class updateBookPayload(BaseModel):
    name: str
    page: int


@app.patch("/books/{book_id}")
def update_book_by_id(req_body: updateBookPayload, book_id: str):
    req_body_dict = req_body.dict()

    name = req_body_dict["name"]
    page = req_body_dict["page"]

    print(f"name: {name}, page: {page}")

    update_message = f"Update book id {book_id} is complete !! "
    response = {"status": "ok", "data": update_message}
    return JSONResponse(content=response, status_code=200)


@app.delete("/books/{book_id}")
def delete_book_by_id(book_id: int):
    delete_message = f"Delete book id {book_id} is complete !! "
    response = {"status": "ok", "data": delete_message}
    return JSONResponse(content=response, status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3001, reload=True)
