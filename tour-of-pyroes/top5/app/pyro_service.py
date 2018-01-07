###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Observable

from .mock_pyroes import Pyroes


class PyroService:

    def get_pyroes(self):
        return Observable.of(Pyroes)

    def get_pyro(self, pyd):
        return Observable.from_(Pyroes).filter(lambda pyro: pyro.pyd == pyd)
