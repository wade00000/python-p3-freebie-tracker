from models import Base, Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)

if __name__ == "__main__":
    import code

    banner = """
    Debug shell for Freebie Tracker

    Available variables:
      - session : SQLAlchemy session
      - Company, Dev, Freebie : your models
    """

    
    vars = globals().copy()
    vars.update(locals())
    code.interact(banner=banner, local=vars)
