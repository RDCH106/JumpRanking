# -*- coding: utf-8 -*-

# 1) Linkero Core
import linkero.core.linkero as linkero
import linkero.core.gateway.gevent_service as gevent
import linkero.core.gateway.waitress_service as waitress

# 2) APIs developed to use with Linkero
import jumprankingAPI

# 3) Load desired APIs
jumprankingAPI.load_jumprankingAPI()

# 4) Run Linkero
if __name__ == "__main__":
    #linkero.run()              # Run with Werkzeug (not recommended for production environments)
    #gevent.run(linkero.app)    # Run with Gevent
    waitress.run(linkero.app)   # Run with Waitress