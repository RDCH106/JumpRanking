# -*- coding: utf-8 -*-

import linkero.core.linkero as linkero
from collections import Iterable


api_base_path = "/jumpranking/api/v1"

# extensions
#db = SQLAlchemy(app)
#linkero.db
record_prototype = {'id': None, 'user': None, 'height': None}


class Record(linkero.db.Model):
    __tablename__ = "records"
    id = linkero.db.Column(linkero.db.Integer, primary_key=True)
    user = linkero.db.Column(linkero.db.String(45))
    height = linkero.db.Column(linkero.db.Integer)

    def __init__(self, user, height):
        self.user = user
        self.height = height

    def __repr__(self):
        return '<Record %r - %r - %r>' % (self.id, self.user, self.height)

    @staticmethod
    def to_json(result):
        data = {}
        records = []
        if isinstance(result, Iterable):
            for record in result:
                records.append(dict(record_prototype, id=record.id, user=record.user, height=record.height))
        else:
            records.append(dict(record_prototype, id=result.id, user=result.user, height=result.height))
        data['data'] = records
        return data


class Register(linkero.Resource):
    def get(self, id):
        ret = Record.query.get(id)
        result = Record.to_json(ret)
        return result


class RegisterList(linkero.Resource):
    def get(self):
        ret = Record.query.all()
        result = Record.to_json(ret)
        return result


##
## Actually setup the Api resource routing here
##
def load_jumprankingAPI():
    linkero.api.add_resource(Register, api_base_path+'/registers/<id>')
    linkero.api.add_resource(RegisterList, api_base_path + '/registers')
