###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component


class DisasterDetailComponent(Component):
    # selector = 'app-root'
    htmlsheet = '''
    <div *_display=edit_did_>
      <h3 [edit_name_]>"{}"</h3>
      <div>
        <label>Id: </label><txt [edit_did_]>{}</txt></div>
      <div>
        <label>Name: </label>
        <input *_fmtvalue=edit_name_ placeholder="name"/>
      </div>
      <p>
        <button (click)=save>Save</button>
        <button (click)="router.route_to('')">Cancel</button>
      </p>
    </div>
    '''

    stylesheet = ''''
    input {
        width: 20em
    }
    '''

    bindings = {
        'edit_name': '',
        'edit_did': 0,
    }

    def loading(self):
        self.disaster_service.get_disaster(self.route.params['did']) \
            .subscribe(self.set_disaster)

    def unloading(self):
        self.set_disaster()

    def set_disaster(self, disaster=None):
        if disaster:
            self.edit_name = disaster.name
            self.edit_did = disaster.did
        else:
            self.edit_name = ''
            self.edit_did = 0

    def save(self):
        # selected is in our parent component
        self.selected.name = self.edit_name
        self.router.route_to('.')

    def can_deactivate(self):
        if not self.edit_did or self.selected.name == self.edit_name:
            return True

        # dialog_service is in the main module
        return self.dialog_service.confirm('Discard changes?')
