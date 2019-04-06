import os


class Config(object):
    PASSWORD = os.environ.get('PASSWORD') or 'ahmednouira'
    MAX_ATTEMPTS = os.environ.get('MAX_ATTEMPTS') or 3
