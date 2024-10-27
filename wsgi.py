import os
from dotenv import load_dotenv
from app import create_app
from app.config import DevelopmentConfig, ProductionConfig

load_dotenv()

environment = os.getenv("ENVIRONMENT")
print(f"ENVIRONMENT: {environment}")

if environment == "development":
    app = create_app(DevelopmentConfig)
elif environment == "production":
    app = create_app(ProductionConfig)
