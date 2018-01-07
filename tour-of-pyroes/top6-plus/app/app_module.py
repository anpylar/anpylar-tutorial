###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Module, Http

from .app_component import AppComponent
from .app_routing import AppRouting
from .pyro_service import PyroService
from .pyro_search import PyroSearchComponent
from .pyro_search_service import PyroSearchService


if False:
    from .mock_pyroes import Pyroes
    Http.serve(Pyroes, index='pyd', url='api/pyroes/')


class AppModule(Module):

    components = AppComponent

    bindings = {}

    services = {
        'pyro_service': PyroService,
        'pyro_search': PyroSearchService,
    }

    routes = AppRouting

    def __init__(self):
        pass
