from pathlib import Path, PurePath

from pydantic_settings import BaseSettings


dir_path = Path(__file__).resolve().parent.parent
env_file_name = ".env"
env_path = PurePath(dir_path, env_file_name)


class Settings(BaseSettings):
    """Получение базовых настроек из переменных окружения"""
    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_DB: str
    MONGODB_USER: str
    MONGODB_PASSWORD: str

    @property
    def MONGODB_URL(self) -> str:
        return f"mongodb://{self.MONGODB_USER}:{self.MONGODB_PASSWORD}@{self.MONGODB_HOST}:{self.MONGODB_PORT}/"

    class Config:
        env_file = env_path
        allow_mutation = False


settings = Settings()
