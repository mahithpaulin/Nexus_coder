import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    MODEL = os.getenv('MODEL', 'claude-3-5-sonnet-20241022')
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', '4096'))
    TEMPERATURE = float(os.getenv('TEMPERATURE', '0.7'))

def validate_config():
    if not Config.ANTHROPIC_API_KEY:
        raise ValueError('ANTHROPIC_API_KEY environment variable is not set')
    return True