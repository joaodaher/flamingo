import os

from sanic import Sanic
from sanic_openapi import swagger_blueprint

import settings
import views

app = Sanic(name='flamingo')
app.update_config(settings)
app.blueprint(swagger_blueprint)

app.blueprint(views.api)


if __name__ == "__main__":
    app.run(host=os.environ.get('HOST', '0.0.0.0'), port=os.environ.get('PORT', 8000))