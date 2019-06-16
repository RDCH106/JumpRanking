# -*- coding: utf-8 -*-

import linkero.core.linkero as linkero


api_base_path = "/jumpranking/api/v1"


class Record(linkero.Resource):
    def get(self, id):
        return 0

##
## Actually setup the Api resource routing here
##
def load_jumprankingAPI():
    linkero.api.add_resource(Record, api_base_path+'/records/<id>')
