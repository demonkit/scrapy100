#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import settings


DeclarativeBase = declarative_base()


def db_connect():
    return sqlalchemy.create_engine(settings.DB_DIALECT)


def createTable(engine):
    DeclarativeBase.metadata.create_all(engine)


site_keyword = sqlalchemy.Table("site_keyword", DeclarativeBase.metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("sid", sqlalchemy.Integer, sqlalchemy.ForeignKey("website.id")),
    sqlalchemy.Column("kid", sqlalchemy.Integer, sqlalchemy.ForeignKey("keyword.id"))
)


class WebSite(DeclarativeBase):
    __tablename__ = 'website'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    domain = sqlalchemy.Column('domain', sqlalchemy.String(256))
    title = sqlalchemy.Column('title', sqlalchemy.String(1000), nullable=True)

    given_url = sqlalchemy.Column('given_url', sqlalchemy.String(1024))
    resp_code = sqlalchemy.Column('resp_code', sqlalchemy.Integer)
    # if spider gets a redirect status, url field will be set
    req_url = sqlalchemy.Column('url', sqlalchemy.String(1024))
    desc = sqlalchemy.Column('desc', sqlalchemy.String(10000), nullable=True)
    scrap_done = sqlalchemy.Column('done', sqlalchemy.Integer, default=0)

    keywords = relationship("Keyword", secondary=site_keyword, backref="parent")

    def __init__(self, domain):
        self.domain = domain

    @staticmethod
    def getByDomain(session, domain):
        return session.query(WebSite).filter(WebSite.domain==domain).first()

    @staticmethod
    def getByGivenUrl(session, given_url):
        return session.query(WebSite).filter(WebSite.given_url==given_url).first()

    @staticmethod
    def getByReqUrl(session, req_url):
        return session.query(WebSite).filter(WebSite.req_url==req_url).first()


class Keyword(DeclarativeBase):
    __tablename__ = 'keyword'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    keyword = sqlalchemy.Column('keyword', sqlalchemy.String(256))

    def __init__(self, kw):
        self.keyword = kw

    @staticmethod
    def get(session, kw):
        obj = session.query(Keyword).filter(Keyword.keyword==kw).first()
        if not obj:
            obj = Keyword(kw)
        return obj
