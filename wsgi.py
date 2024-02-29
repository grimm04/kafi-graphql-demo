import os 

from src.main import create_app  
from src.main.database.init_db import init_db

app = create_app(os.getenv('FLASK_ENV') or 'dev')  

def main():
    # init_db()
    app.run(host='0.0.0.0')
 
if __name__ == '__main__': 
    main()