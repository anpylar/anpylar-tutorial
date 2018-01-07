###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component


class AdminComponent(Component):
    htmlsheet = '''
    <h3>ADMIN</h3>
    <nav>
      <a routerLink="" routerLinkActive="active">Dashboard</a>
      <a routerLink="disasters" routerLinkActive="active">Manage Disasters</a>
      <a routerLink="pyroes" routerLinkActive="active">Manage Pyroes</a>
    </nav>
    <router-outlet></router-outlet>
    '''
