###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from .dashboard import DashboardComponent
from .pyro_detail import PyroDetailComponent
from .pyroes import PyroesComponent


AppRouting = [
    {
        'path': '',
        'redirect_to': '/dashboard',
        'path_match': 'full'
    },
    {
        'path': 'dashboard',
        'component': DashboardComponent
    },
    {
        'path': 'pyroes',
        'component': PyroesComponent
    },
    {
        'path': 'detail',
        'component': PyroDetailComponent,
        'params': {'pyd': int},  # param transformation function
    },
]
