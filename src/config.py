import os
import starkbank
from dotenv import load_dotenv

# Getting .env file content
load_dotenv()
private_key_content = os.getenv("PRIVATE_KEY")
project_id = os.getenv("PROJECT_ID")

# Setting up credentials
project = starkbank.Project(
    environment="sandbox",
    id=project_id,
    private_key=private_key_content
)