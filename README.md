# FastAPI - Python Framework for AI

FastAPI is Python Framework for Backend which receive HTTP request and call python funtion then return response

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

- Install FastApi & Dependencies 
  ```bash 
  pip install fastapi uvicorn pydantic python-dotenv httpx requests
  ```

- Create a virtual environment for Windows
  ```bash
  python -m venv venv
  ```

- Activate virtual environment
  ```bash 
  `venv\Scripts\activate`
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

### API Endpoint - http://127.0.0.1:8000
### Swagger UI - http://127.0.0.1:8000/docs

## Pydantic 
- It is used for Validation for data that is sent through request and response
- Syntax : 
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

## Project Architecture 
```bash
├──app/
│   ├── main.py
│   │
│   ├── database.py
│   │
│   ├── schemas.py
│   │
│   ├── models.py
│   │
│   ├── config.py
│   │
│   ├── routers/
│   │      users.py
│   │
│   ├── services/
│   │      user_service.py
│   │
│   ├── repositories/
│   │      user_repository.py
│   │
│   └── utils/
│   
├── example.env
│
├── .env
│
├── README.md
│
├── sqlite.db
│
├── requirements.txt
│
└──  .gitignore 
```

## Dependncy Injection
- FastAPI uses a powerful Dependency Injection (DI) system. Instead of your API endpoints manually creating the services or database connections they need, FastAPI automatically instantiates and provides ("injects") them at runtime using Depends()
- It has Loose Coupling, High Modularity, Automatic Lifecycle Management, Effortless Testing

```bash
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
```
```bash
@app.post("/users")
async def create_user(user_data: CreateUser, db: Session = Depends(get_db)):

```
- When a user sends a request to the /users endpoint:
  1. Interception: FastAPI stops and looks at Depends(get_db) 
  2. Execution: FastAPI runs get_db(), which opens a fresh database session
  3.Injection: FastAPI injects that active session directly into your db: Session parameter 
  4. Execution: Your endpoint code runs safely using the provided database session 
  5. Cleanup: Once the response is sent back to the user, FastAPI executes the finally block to automatically close the database connection, preventing memory leaks.

## Environment Variable
- Instead of hardcoding sensitive values directly in code we store them in env file 
  ```bash
  pip install python-dotenv
  ```
- Then we access it in config file and export it
  ```bash
  from pydantic_settings import BaseSettings, SettingsConfigDict

  class Settings(BaseSettings):
      app_name: str = "AI Backend Journey"
      debug: bool = True
      OPENAI_API_KEY: str  
 
      model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

  settings = Settings()
  ```

## SQLAlchemy
- SQLAlchemy is Object Relation Mapping (ORM)
- Database use SQL and Python use Objects so, SQLAlchemy translate Python Object into SQL
- Install Command:
  ```bash
  pip install sqlalchemy pydantic-settings
  ```

## Modular Architecture Explain

### Router Layer
- Router Layer only handle HTTP Request 
- Router Layer paased request data to Service Layer

### Service Layer
- Service Layer Containe Business Logic
- Service Layer use repository layer to perform db opeartion

### Repository Layer
- Interacts directly with SQLAlchemy to convert Python object code into optimized SQL queries.
- Executes database operations and returns standard SQLAlchemy Models as the initial response.

### DataBase Layer
- Manages the connection pool and configuration details for the database engine.
- Handles the actual execution of SQL statements sent by the Repository Layer.