
from sqlalchemy import create_engine


import logging
import os
from decouple import config





BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
DATABASES = {
     
        'ENGINE':config('DB_ENGINE'),
        'NAME':config('DB_NAME'),
        'USER':config('DB_USER'),
        'PASSWORD':config('DB_PASSWORD'),
        'HOST':config('DB_HOST'),
        'PORT':config('DB_PORT'),
    }



def connectionBD():

    # logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    logging.info("Init connect")
    engine = DATABASES["ENGINE"]
    user = DATABASES["USER"]
    pasdb = DATABASES["PASSWORD"]
    host_db = DATABASES["HOST"]
    port_db= DATABASES['PORT']
    name_db = DATABASES["NAME"]

    # Esquema: create_engine('mysql+mysqlconnector://user:password@host:port/database')
    url_db = f'{engine}://{user}:{pasdb}@{host_db}:{port_db}/{name_db}'
    

    try:
        print(url_db)
       
        engine = create_engine(url=url_db, echo=False)

        logging.info("connection success")
        return engine
    except Exception as e:
        print(f"Error: {e}")
        logging.warning('Not connection')
        return None
       

if __name__=='__main__':
    engine=connectionBD()
    print("RETURN")
    print(type(engine))
    
    
    if engine!= None:
        print("YES")
        print(engine.connect())
        pass
    
   
