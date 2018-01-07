###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Observable, Model


class Disaster(Model):
    bindings = {
        'did': 0,
        'name': '',
    }


DISASTERS = [
    Disaster(**{'did': 1, 'name': 'The Python Menace'}),
    Disaster(**{'did': 2, 'name': 'Revenge of the Pyth'}),
    Disaster(**{'did': 3, 'name': 'The Empyre pykes back'}),
    Disaster(**{'did': 4, 'name': 'No more Pyzzas for the films!'}),
]


class DisasterService:
    next_disaster_id = 100

    def __init__(self):
        self.disasters_ = Observable.of(DISASTERS)

    def get_disasters(self):
        return self.disasters_

    def get_disaster(self, did):
        return self.get_disasters() \
            .map(lambda disasters: [c for c in disasters if c.did == did]) \
            .filter(lambda disasters: len(disasters)) \
            .map(lambda disasters: disasters[0])

    def add_disaster(self, name):
        disaster = Disaster(did=self.next_disaster_id, name=name)
        self.next_disaster_id += 1

        DISASTERS.append(disaster)
        self.disasters_ = o = Observable.of(DISASTERS)
        return o
