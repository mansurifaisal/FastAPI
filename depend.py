from typing import Annotated
from fastapi import FastAPI, Depends, Cookie

app = FastAPI()

def query_extractor(q: str | None = None):
    return q

def query_or_coockie_extractor(
        q: Annotated[str, Depends(query_extractor)],
        last_query: Annotated[str | None, Cookie()] = None,):
    if not q:
        return last_query
    return q

@app.get("/items/")
async def read_query(
        query_or_default: Annotated[str, Depends(query_or_coockie_extractor)]
):
    return {"q_or_cookie": query_or_default}
