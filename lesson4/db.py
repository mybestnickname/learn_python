from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///mybase.db')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(120), unique=True)

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)



class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(140))
    image = Column(String(500))
    published = Column(DateTime)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

def __repr__(self):
        return '<Post {}>'.format(self.title)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

