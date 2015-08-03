from datetime import datetime

from flaskBase.db import db


def serial_from(obj, add_fields=[], add_class_fields=[]):
    if isinstance(obj, BaseModel):
        add_class_fields_dicts = []
        for add_field in add_class_fields:
            add_field_split = add_field.split('.')
            if len(add_field_split) == 2:
                class_name = add_field_split[0]
                attribute_name = add_field_split[1]
                add_class_fields_dicts.append({
                    'class': class_name,
                    'attribute': attribute_name
                })
        value_add_fields = []
        for add_class_field in add_class_fields_dicts:
            if add_class_field['class'] == obj.__class__.__name__:
                # Instance is of class, let's add field
                value_add_fields.append(add_class_field['attribute'])
        add_fields = add_fields + value_add_fields
        return obj.to_serializable_dict(add_fields=add_fields, add_class_fields=add_class_fields)
    elif isinstance(obj, list):
        return [serial_from(elem, add_fields=add_fields, add_class_fields=add_class_fields) for elem in obj]
    elif isinstance(obj, dict):
        return {key: serial_from(value, add_class_fields=add_class_fields) for key, value in obj.iteritems()}
    else:
        return obj


class BaseModel(object):
    created_at_utc = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at_utc = db.Column(db.DateTime, onupdate=datetime.utcnow)

    __public__ = []

    def to_serializable_dict(self, add_fields=[], add_class_fields=[]):
        dictionary = {}
        add_class_fields_dicts = []
        for add_field in add_class_fields:
            add_field_split = add_field.split('.')
            if len(add_field_split) == 2:
                class_name = add_field_split[0]
                attribute_name = add_field_split[1]
                add_class_fields_dicts.append({
                    'class': class_name,
                    'attribute': attribute_name
                })

        for public_key in self.__public__ + add_fields:
            value = getattr(self, public_key)
            if value or isinstance(value, int) or isinstance(value, float):
                if isinstance(value, BaseModel):
                    # If this is a class to which we
                    # want to add fields, let's add them now
                    value_add_fields = []
                    for add_class_field in add_class_fields_dicts:
                        if add_class_field['class'] == value.__class__.__name__:
                            # Instance is of class, let's add field
                            value_add_fields.append(add_class_field['attribute'])
                    value = value.to_serializable_dict(add_fields=value_add_fields, add_class_fields=add_class_fields)
                if isinstance(value, datetime):
                    value = value.isoformat()
                if isinstance(value, list):
                    value = [elem.to_serializable_dict(add_class_fields=add_class_fields) if hasattr(elem, 'to_serializable_dict') else elem for elem in value]
                dictionary[public_key] = value
        return dictionary

    def __repr__(self):
        return unicode(self).encode('utf-8')
