#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import settings


DeclarativeBase = declarative_base()


def db_connect():
    return sqlalchemy.create_engine(URL(**settings.DATABASE))


def createTable(engine):
    DeclarativeBase.metadata.create_all(engine)


class WebSite(DeclarativeBase):
    __tablename__ = 'website'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    url = sqlalchemy.Column('url', sqlalchemy.String(256))
    title = sqlalchemy.Column('title', sqlalchemy.String(1000), nullable=True)
    desc = sqlalchemy.Column('desc', sqlalchemy.String(1000), nullable=True)


class Keyword(DeclarativeBase):
    __tablename__ = 'keyword'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    keyword = sqlalchemy.Column('keyword', sqlalchemy.String(256))
