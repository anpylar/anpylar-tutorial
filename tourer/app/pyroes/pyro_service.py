###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Observable, Model


class Pyro(Model):
    bindings = {
        'pyd': 0,
        'name': '',
    }


_PYROES = [
    {'pyd': 11, 'name': 'Pyro Nakamura'},
    {'pyd': 12, 'name': 'Mopynder Shuresh'},
    {'pyd': 13, 'name': 'Pyter Pytrelli'},
    {'pyd': 14, 'name': 'Angela Pytrelli'},
    {'pyd': 15, 'name': 'Claire Pynnet'},
    {'pyd': 16, 'name': 'Noah Pynnet'},
    {'pyd': 17, 'name': 'Pysaac Mendez'},
    {'pyd': 18, 'name': 'Pyki Sanders'},
    {'pyd': 19, 'name': 'The Pytian'},
    {'pyd': 20, 'name': 'Pylar'},
]

PYROES = [Pyro(**p) for p in _PYROES]


class PyroService:
    def get_pyroes(self):
        return Observable.of(PYROES)

    def get_pyro(self, pyd):
        self.pyd = pyd
        return self.get_pyroes() \
            .map(self.filter_pyroes)

    def filter_pyroes(self, pyroes):
        return [p for p in pyroes if p.pyd == self.pyd][0]
