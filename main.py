import os
from dotenv import load_dotenv

load_dotenv()
mode = os.environ.get("APP_MODE", "development")
print(f"Приложение запущено в режиме: {mode}")
