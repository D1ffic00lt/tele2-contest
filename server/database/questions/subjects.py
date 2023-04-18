import sqlalchemy

from ..db_session import SqlAlchemyBase

__all__ = ("Subject", )


class Subject(SqlAlchemyBase):
    __tablename__ = 'subjects'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True
    )
    subject = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )
