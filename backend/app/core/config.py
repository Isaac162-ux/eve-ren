from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "E.V.E.9"
    environment: str = "development"
    host: str = "0.0.0.0"
    port: int = 8000
    allowed_hosts: str = "localhost,127.0.0.1"
    cors_origins: str = "http://localhost:8000,http://127.0.0.1:8000"
    provider: str = "ollama"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"
    ollama_timeout: float = 90.0
    memory_db_path: str = "./data/eve_memory.db"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    @property
    def allowed_hosts_list(self): return [x.strip() for x in self.allowed_hosts.split(",") if x.strip()]
    @property
    def cors_origins_list(self): return [x.strip() for x in self.cors_origins.split(",") if x.strip()]
@lru_cache
def get_settings() -> Settings: return Settings()
