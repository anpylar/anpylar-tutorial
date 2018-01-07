###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Module

from ..auth_guard_service import AuthGuard

from .admin_component import AdminComponent
from .admin_dashboard_component import AdminDashboardComponent
from .manage_disasters_component import ManageDisastersComponent
from .manage_pyroes_component import ManagePyroesComponent


class AdminModule(Module):
    routes = [{
        'path': '',
        'component': AdminComponent,
        'can_activate': AuthGuard,
        'children': [{
            'path': '',
            'children': [
                {'path': 'disasters', 'component': ManageDisastersComponent},
                {'path': 'pyroes', 'component': ManagePyroesComponent},
                {'path': '', 'component': AdminDashboardComponent}
            ]
        }]
    }]
