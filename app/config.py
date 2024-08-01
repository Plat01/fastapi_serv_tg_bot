from pydantic import PostgresDsn, RedisDsn
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env" if __name__ == '__main__' else ".env",
        env_ignore_empty=True,
        extra="ignore"
    )

    SERVICE_NAME: str
    NOTIFICATION_ID: int

    BOT_TOKEN: str

    DB_ENGINE: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme=self.DB_ENGINE,
            username=self.DB_USERNAME,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            path=self.DB_NAME,
        )

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DATABASE: int


    @property
    def REDIS_URL(self) -> RedisDsn:
        return RedisDsn.build(
            scheme="redis",
            host=self.REDIS_HOST,
            port=self.REDIS_PORT,
            path=f"/{self.REDIS_DATABASE}"
        )

    def _get_redis_url(self, db_index: int) -> RedisDsn:
        return RedisDsn.build(
            scheme="redis",
            host=self.REDIS_HOST,
            port=self.REDIS_PORT,
            path=f"{db_index}"
        )

    @property
    def CELERY_BROKER_URL(self) -> RedisDsn:
        return self._get_redis_url(1)

    @property
    def CELERY_RESULT_BACKEND(self) -> RedisDsn:
        return self._get_redis_url(2)


settings = Settings()


if __name__ == '__main__':
    stngs = Settings()
    print(stngs.CELERY_BROKER_URL)
