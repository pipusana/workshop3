from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field


@app.get("/profile/{name}")
def get_path_parameter(name: str = Path("", max_length=10)):
    return JSONResponse(
        content={"message": f"My name is: {name}"},
        status_code=200,
    )


default_string = ""
default_int = 0


class Books(BaseModel):
    name: str = Field(default_string, title="Book name", max_length=300)
    page: int = Field(default_int, title="Page in book", max_length=300)


@app.post("/books")
def create_books(req_body: Books):
    mock_response = {
        "_id": 4,
        "name": req_body.name,
        "page": req_body.page,
    }
    return JSONResponse(
        content={"status": "ok", "data": mock_response}, status_code=201
    )