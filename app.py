"""This is an example app, demonstrating usage."""

import os
import settings

from flask import Flask,jsonify

import jinja2
from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request,session, send_from_directory, url_for)

from flask_jsondash import charts_builder,static, templates

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'someoneknowyouisntit'
app.config.update(
    JSONDASH_FILTERUSERS=False,
    JSONDASH_GLOBALDASH=True,
    JSONDASH_GLOBAL_USER='global',
)

app.debug = True

app.register_blueprint(charts_builder.charts,url_prefix='/')

from api import app as api
app.register_blueprint(api,url_prefix='/api/')

from serviceapi import app as serviceapi
app.register_blueprint(serviceapi,url_prefix='/service/')

from example import app as example
app.register_blueprint(example,url_prefix='/example/')



def _can_edit_global():
    return True


def _can_delete():
    return True


def _can_clone():
    return True


def _get_username():
    return 'anonymous'


# Config examples.
app.config['JSONDASH'] = dict(
    metadata=dict(
        created_by=_get_username,
        username=_get_username,
    ),
    static=dict(
        js_path='js/vendor/',
        css_path='css/vendor/',
    ),
    auth=dict(
        edit_global=_can_edit_global,
        clone=_can_clone,
        delete=_can_delete,
    )
)

@app.route('/', methods=['GET'])
def index():
    """Sample index."""
    return '<h1><a href="/example/chartit">example.</a><br><a href="/charts/">setting.</a></h1>'


if __name__ == '__main__':
    PORT = int(os.getenv('PORT', 8080))
    HOST = os.getenv('HOST', '0.0.0.0')
    app.run(debug=True, host=HOST, port=PORT)


