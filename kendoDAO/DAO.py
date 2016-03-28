from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
class DAO():
    def __init__(self):
        self.session = None
        try:
            engine = create_engine('sqlite:///bd.db', echo=True)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as err:
            raise Exception(err.message)

