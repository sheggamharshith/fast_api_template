from pydantic import (
    BaseSettings,
    PostgresDsn,
    Field,
    AnyHttpUrl,
)
from typing import (List)
import os


class BaseSettings(BaseSettings):
    """
    # doc setting 
    url: https://fastapi.tiangolo.com/advanced/settings/?h=practice#the-main-app-file

    This is basic configuration setting for the fast api 
    use the lru_cache to get redundant import of setting 
    on every call

    # example
    @lru_cache()
    def get_settings():
        return config.Settings()


    """

    # Change this at production
    secret_key: str = Field(..., env='SECRET_KEY')

    # database need to find ways to change the settings taking dynamicallye
    pg_dsn: PostgresDsn = Field(..., env='DB_URL')

    apps: List[str] = ["user", "auth", "base"]

    base_dir: str = os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))


    #--cors---
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost.tiangolo.com",
                                              "https://localhost.tiangolo.com",
                                              "http://localhost",
                                              "http://localhost:8080", ]

    # --- debug -----
    debug: bool = False

    # ---  CORS ---

    # ---- JWT -----

    jwt_secret_key: str = Field(..., env='JWT_SECRET_KEY')
    jwt_algo : str = Field(..., env='JWT_ALGORITHM')

    # --- EMail ----

    # --- project name ---

    project_name: str = Field("FastApi_project", env='PROJECT_NAME')

    class Config:
        # change the default prefix if you want to change defaults to no prefix, i.e. ""
        env_prefix = 'my_prefix_'
        # need to check its not taking the absolute path
        env_file = "/home/sheggam/Desktop/fast_api_template/.env"


if __name__ == "__main__":
    print(BaseSettings().dict())
