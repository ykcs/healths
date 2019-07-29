import sae

from health import app

application = sae.create_wsgi_app(app)