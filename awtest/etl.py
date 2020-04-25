import requests
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.dialects.postgresql import JSON
from contextlib import contextmanager
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres:postgres@db/test')
if not database_exists(engine.url):
    create_database(engine.url)


class Profile(Base):
    __tablename__ = 'profile'
    user_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    gender = Column(String(8))
    name = Column(JSON)
    location = Column(JSON)
    email = Column(String(80))
    login = Column(JSON)
    dob = Column(JSON)
    registered = Column(JSON)
    id = Column(JSON)
    phone = Column(String(16), nullable=False)
    cell = Column(String(16), nullable=False)
    picture = Column(JSON)
    nat = Column(String(2))

    def __repr__(self):
        return f"Profile #{self.user_id}, name: {self.name['first']} {self.name['last']}, age {self.dob['age']}"

    def to_dict(self):
        prof_dict = {}
        for attr in vars(self):
            if attr.startswith('_'):
                continue
            attr_value = getattr(self, attr)
            prof_dict[attr] = attr_value
        return prof_dict


Base.metadata.create_all(engine)


def get_profiles_from_api(**kwargs):
    try:
        url = 'https://randomuser.me/api/'
        res = requests.get(url, params=kwargs)
        res.raise_for_status()
        return res.json()['results']
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


@contextmanager
def session_scope():
    DBSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    session = DBSession()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()


def write_data(data):
    with session_scope() as s:
        for elem in data:
            s.add(Profile(**elem))
        s.commit()


def get_all_profiles():
    with session_scope() as s:
        return s.query(Profile).all()


def get_one_entity(id):
    with session_scope() as s:
        return s.query(Profile).get(id)


def delete_profile(id):
    with session_scope() as s:
        s.query(Profile.id == id).delete()
        s.commit()
        return {'message': f'User #{id} successfully deleted'}


if __name__ == '__main__':
    profiles = get_profiles_from_api(results=100, gender='male')
    write_data(profiles)
