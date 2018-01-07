###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import http, Observable

from .pyro import Pyro

import json


class PyroSearchService:
    def __init__(self):
        self.http = http.Http(
            url='api/pyroes/',
            headers={'Content-Type': 'application/json'},
        )

    def search(self, term):
        return self.http.get(data={'name': term}) \
            .map(lambda x: [Pyro(**p), for p in json.loads(x)])
