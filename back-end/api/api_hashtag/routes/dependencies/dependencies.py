import sys
import os
from models.models import db
from sqlalchemy.orm import sessionmaker

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)

def pegar_sessao():
    try:    
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close