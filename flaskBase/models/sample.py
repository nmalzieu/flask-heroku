from flaskBase.db import db
from flaskBase.models import BaseModel


class SampleModel(BaseModel, db.Model):
    __tablename__ = 'sample_model'
    __public__ = [
        'created_at_utc',
        'updated_at_utc',
        'id'
    ]

    id = db.Column(db.BigInteger, primary_key=True)

    def __unicode__(self):
        return u'<SampleModel %s>' % self.id
