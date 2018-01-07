###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Observable, http

from .pyro import Pyro

import json


class PyroService:

    def __init__(self):
        self.http = http.Http(
            url='api/pyroes/',
            headers={'Content-Type': 'application/json'},
        )

    def handle_error(self, e, retval=False):
        print(e)
        return retval

    def get_pyroes(self):
        return self.http.get() \
            .map(lambda x: [Pyro(**p), for p in json.loads(x)]) \
            .catch_exception(lambda e: self.handle_error(e, []))

    def get_pyro(self, pyd):
        return self.http.get(url='{}'.format(pyd)) \
            .map(lambda x: Pyro(**json.loads(x))) \
            .catch_exception(lambda e: self.handle_error(e, Pyro()))

    def update_pyro(self, pyro):
        return self.http.put(url='{}'.format(pyro.pyd),
                             data=json.dumps({'name': pyro.name})) \
            .catch_exception(lambda e: self.handle_error(e))

    def delete_pyro(self, pyd):
        return self.http.delete(url='{}'.format(pyd)) \
            .catch_exception(lambda e: self.handle_error(e))

    def add_pyro(self, name):
        return self.http.post(data=json.dumps({'name': name})) \
            .map(lambda x: Pyro(**json.loads(x))) \
            .catch_exception(lambda e: self.handle_error(e))
