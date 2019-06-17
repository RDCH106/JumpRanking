# -*- coding: utf-8 -*-

import linkero.core.linkero as linkero


api_base_path = "/jumpranking/api/v1"

# extensions
#db = SQLAlchemy(app)
#linkero.db


class Record(linkero.db.Model):
    __tablename__ = "records"
    id = linkero.db.Column(linkero.db.Integer, primary_key=True)
    user = linkero.db.Column(linkero.db.String(45))
    height = linkero.db.Column(linkero.db.Integer)

    def __init__(self, user, height):
        self.user = user
        self.height = height

    def __repr__(self):
        return '<Record %r - %r -%r -%r>' % (self.id, self.user, self.height)


class Record(linkero.Resource):
    def get(self, id):
        return 0

##
## Actually setup the Api resource routing here
##
def load_jumprankingAPI():
    linkero.api.add_resource(Record, api_base_path+'/records/<id>')
