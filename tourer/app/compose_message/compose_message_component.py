###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component


class ComposeMessageComponent(Component):
    bindings = {
        'details': '',
        'msg': '',
    }

    def unloading(self):
        # return to default state when unloading for next load
        self.details = ''
        self.msg = ''

    def render(self, node):
        d = node.select('div[name="details"]')  # will get first
        d._display(bool(self.details_))
        d._fmt(details=self.details_)

        t = node.select('textarea')._fmtvalue(self.msg_)

        p = node.select('p[name="buttons"]')
        p._display(self.details_ == '')
        bsend = node.select('button[name="send"]')
        bsend._bindx.click(self.send)
        bcancel = node.select('button[name="cancel"]')
        bcancel._bindx.click(self.close_popup)

    def send(self):
        self.details = 'Sending Message ...'
        # the message would be available in self.msg

        Observable.of(True) \
            .delay(2000) \
            .subscribe(self.close_popup)

    def close_popup(self, close=True):
        self.close_outlet()
