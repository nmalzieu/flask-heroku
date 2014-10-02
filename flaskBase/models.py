from sqlalchemy.sql import func
from datetime import datetime

from db import db


def serial_from(obj):
    if isinstance(obj, BaseModel):
        return obj.to_serializable_dict()
    elif isinstance(obj, list):
        return [serial_from(elem) for elem in obj]
    elif isinstance(obj, dict):
        return {key: serial_from(value) for key, value in obj.iteritems()}
    else:
        return obj


class BaseModel(object):
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    __public__ = None

    def to_serializable_dict(self):
        dictionary = {}
        for public_key in self.__public__:
            value = getattr(self, public_key)
            if value:
                if isinstance(value, BaseModel):
                    value = value.to_serializable_dict()
                if isinstance(value, datetime):
                    value = value.isoformat()
                if isinstance(value, list):
                    value = [elem.to_serializable_dict() for elem in value]
                dictionary[public_key] = value
        return dictionary

    def __repr__(self):
        return unicode(self).encode('utf-8')


class SampleModel(BaseModel, db.Model):
    __tablename__ = 'sample_model'
    __public__ = ['created_at', 'updated_at', 'id']

    id = db.Column(db.BigInteger, primary_key=True)

    def __unicode__(self):
        return u'<SampleModel %s>' % self.fullname
