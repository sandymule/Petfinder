# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import logging.config

import tornado.ioloop
import tornado.web
from tornado.options import options

from sklearn.externals import joblib

from . import handler

def main():

    # Get the Port and Debug mode from command line options or default in settings.py
    options.parse_command_line()


    # create logger for app
    logger = logging.getLogger('app')
    logger.setLevel(logging.INFO)

    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT)

    # Load ML Models
    logger.info("Loading IRIS Prediction Model...")

    urls = [
        (r"/$", handler.IndexHandler),
        (r"/recommend$", handler.RecommendHandler)
    ]

    # Create Tornado application
    application = tornado.web.Application(
        urls,
        static_path='app/static',
        debug=True,
        autoreload=True)

    # Start Server
    logger.info("Starting App on Port: {}".format(9000))
    application.listen(9000)
    tornado.ioloop.IOLoop.current().start()