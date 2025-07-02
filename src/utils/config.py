from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')  

USER_LINKEDIN = os.getenv('USER_LINKEDIN')  
PASSWORD_LINKEDIN = os.getenv('PASSWORD_LINKEDIN')
