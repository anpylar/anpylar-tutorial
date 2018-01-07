###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Module
from .pyroes import PyroesComponent
from .pyro_detail import PyroDetailComponent
from .pyro_service import PyroService, Pyro


class PyroesModule(Module):

    services = {
        'pyro_service': PyroService,
    }

    routes = [
        {'path': 'pyroes', 'redirect_to': '/superpyroes'},
        {'path': 'superpyroes', 'component': PyroesComponent},
        {
            'path': 'pyro',
            'redirect_to': '/superpyro'},
        {
            'path': 'superpyro',
            'params': {'pyd': int},
            'component': PyroDetailComponent,
        }
    ]

    def __init__(self):
        pass
