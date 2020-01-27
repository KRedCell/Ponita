import asyncio
import json
import math
import random
import threading
import time
from os import path

from flask import Blueprint, Flask, g, jsonify, session
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

import Authorization
from .configs.Config import UserConfig
from DynamicEventLoop import DynamicEventLoop
from Pointa import Player, Pointa
from webapp import app, Data


def init_app(config):
    # Init the app
    app.config.from_object(UserConfig)
    return app


def Serve(port: int):
    httpServer = HTTPServer(WSGIContainer(init_app(UserConfig)))
    httpServer.listen(5000)
    IOLoop.instance().start()
