from marshmallow import Schema, fields, pre_dump, post_load
from types import SimpleNamespace

class ObjectSchema(Schema):

    @post_load(pass_many=True)
    def make_namespace(self, data, many, **kwargs):
        if (many):
            return [SimpleNamespace(**d) for d in data]
        return SimpleNamespace(**data)
            

    @pre_dump(pass_many=True)
    def make_dict(self, data, many, **kwargs):
        if many:
            return [vars(d) for d in data]
        return vars(data)