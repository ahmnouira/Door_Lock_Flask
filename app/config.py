import os         # import system lib

class Config(object):
    PASSWORD = os.environ.get("PASSWORD") or "ahmnouira" #change "ahmnouira" as you wish or set it by 'export'
    MAX_ATTEMPTS = os.environ.get("MAX_ATTEMPTS") or 2   # 0-->2 = 3 attempts  
