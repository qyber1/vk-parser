from pydantic_settings import BaseSettings



def get_token() -> str:
    class Settings(BaseSettings):
        ACCESS_TOKEN: str

        class Config:
            env_file = '.env'

    settings = Settings()
    return settings.ACCESS_TOKEN