from flask import Flask
from api.routes.controllers import api

def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.DevelopmentConfig')
    app.register_blueprint(api, url_prefix='/api')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
