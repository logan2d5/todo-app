from fastapi import FastAPI
from pydantic import BaseModel
from main import data


class ToDo(BaseModel):
    id: str | None = None
    title: str
    completed: bool


todo_api = FastAPI()
prefix = '/api'


@todo_api.get(prefix + '/todos')
async def todos():
    return data.read_all()


@todo_api.get(prefix + '/todos/{todo_id}')
async def todos(todo_id: str):
    return data.read(todo_id)


@todo_api.delete(prefix + '/todos/{todo_id}')
async def todos(todo_id: str):
    return data.delete(todo_id)


@todo_api.put(prefix + '/todos/{todo_id}', response_model=ToDo)
async def todos(todo_id: str, todo: ToDo):
    return data.update(todo_id, **dict(todo))


@todo_api.post(prefix + '/todos/', response_model=ToDo)
async def todos(todo: ToDo):
    return data.create(**dict(todo))
