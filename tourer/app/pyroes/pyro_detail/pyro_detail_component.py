###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component, html
from ..pyro_service import Pyro


class PyroDetailComponent(Component):
    htmlsheet = '''
    <h2>PyRoeS</h2>
    <!-- <div *_display=pyro_.pyd_> -->
    <div>
      <h3 {name}=pyro_.name_>"{name}"</h3>
      <div>
        <label>Pyd: </label><txt {pyd}=pyro_.pyd_>{pyd}</txt>
      </div>
      <div>
        <label>Name: </label>
        <input *_fmtvalue=pyro_.name_ placeholder="name"/>
      </div>
      <p>
        <button (click)="router.route_to('/pyroes')">Back</button>
        <!-- <button (click)="goto_pyroes()">Back</button> -->
      </p>
    </div>
    '''

    stylepath = None

    bindings = {
        'pyro': Pyro(),
    }

    def loading(self):
        self.pyro_service.get_pyro(self.route.params['pyd']) \
            .subscribe(self.pyro_)

    def unloading(self):
        self.pyro = Pyro()

    def render(self, node):
        pass

    def goto_pyroes(self):
        self.router.route_to('/pyroes')  # route without params
