###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component


class AppComponent(Component):
    htmlsheet = '''
    <h1 class="title">AnPyLar Tourer</h1>
    <nav>
      <a routerLink="/disaster-center" routerLinkActive="active">Disaster Center</a>
      <a routerLink="/superpyroes" routerLinkActive="active">Pyroes</a>
      <a routerLink="/admin" routerLinkActive="active">Admin</a>
      <a routerLink="/login" routerLinkActive="active">Login</a>
      <a routerLink="/compose" routerLinkActive="active">Contact</a>
    </nav>
    <router-outlet></router-outlet>
    <router-outlet name="popup"></router-outlet>
    '''

    stylepath = None
