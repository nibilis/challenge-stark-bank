import starkbank
from dotenv import load_dotenv
import os

# Getting .env file content
load_dotenv()
private_key_content = os.getenv("PRIVATE_KEY")

# Setting up credentials
project = starkbank.Project(
    environment="sandbox",
    id="6215376505405440",
    private_key=private_key_content
)
