from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AI Backend Journey"
    debug: bool = True
    OPENAI_API_KEY: str 
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    SECRET_KEY:str
    ALGORITHM:str
 
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
