#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright 2013 Alexandre Bulté <alexandre[at]bulte[dot]net>
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from flask import Flask, render_template
from flask_fanstatic import Fanstatic

# configuration
DEBUG = True
FANSTATIC_OPTIONS = {'bottom': True, 'minified': True}

app = Flask(__name__)
app.config.from_object(__name__)
fanstatic = Fanstatic(app)

# define your own ressources this way
fanstatic.resource('js/app.js', name='app_js', bottom=True)

@app.route('/')
def index():
    return render_template('index.html')