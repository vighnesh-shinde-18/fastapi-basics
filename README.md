# FastAPI - Python Framework for AI

FastAPI is Python Framework for Backend which receiver HTTP request and call python funtions then return response

## Features
- Modern
- Automatic validation
- Faster
- Swagger UI built in
- Full type hints

## Steps for Setup
- Create project
  ```bash
  cd ai-backend-journey
  ```

- Create virtual environment for Windows
  ```bash
  python -m venv venv
  ```

- Activate virtual environment
  ```bash 
  venv\Scripts\activate
  ```

- Install packages
  ```bash 
  pip install fastapi uvicorn
  ```

- Save dependencies
  ```bash 
  pip freeze > requirements.txt
  ```

- Deactivate virtual environment
  ```bash 
  deactivate
  ``` 

## Run Server
  ```bash
  uvicorn app.main:app --reload
  ```

### API end Point - http://127.0.0.1:8000
### Swagger UI - http://127.0.0.1:8000/docs

## Pydantic 
- It Use for Validation for data which send through request and response
- Syntex : 
    ```bash
    from pydantic import BaseModel, Field
    class schema(BaseModel):
    language: str
    code: str = Field(..., min_length=10)
    max_tokens: int = 500
    ``` 
- Then we use them like this :-
  ```bash
  from app.schemas import CodeSubmission
  @app.post("/",response_model=CodeSubmission)
  async def submit(code:CodeSubmission)
  ```

## Router
- Syntax:
  creating router
  ```bash
  router = APIRouter(prefix="/users", tags=["Users"])
  ```
  importing and using router
  ```bash
  from app.routers.users import router as users_router
  app.include_router(users_router)
  ```