from anpylar import Model, Module, Component, html, Observable


class Pyro(Model):
    bindings = {
        'pyd': 0,
        'name': '',
    }


_PYROES = [
    {'pyd': 11, 'name': 'Pyro Nakamura'},
    # {'pyd': 12, 'name': 'Mopynder Shuresh'},
]

PYROES = [Pyro(**p) for p in _PYROES]


class PyroDetailComponent(Component):
    htmlsheet = '''
    <div>
      <h3 {name}=pyro_.name_>"{name}"</h3>
      </p>
    </div>
    '''

    bindings = {
        'pyro': Pyro(),
    }

    def loading(self):
        pyd = self.route.params['pyd']
        print('pyd from params is:', pyd)
        for p in PYROES:
            if p.pyd == pyd:
                self.pyro_(p)
                break

    def unloading(self):
        self.pyro = Pyro()


class PyroesComponent(Component):
    htmlsheet = '''
    <h2>Pyroes</h2>
    <ul class="items"></ul>
    '''

    bindings = {
        'pyd': 0,
        'pyroes': [],
    }

    def loading(self):
        self.pyroes = PYROES

    def unloading(self):
        self.pyroes = []

    def li_pyroes(self, pyroes):
        print('li_pyroes called with:', pyroes)
        for pyro in pyroes:
            with html.li() as li:
                # li._class.selected(self.selected_.pyd_ == pyro.pyd)
                li._class.selected(self.pyd == pyro.pyd)

                # self.pyd_
                # .map(lambda x: x == pyro.pyd)
                # .do_action(lambda x: print('HERE IS THE PROBLEM:', x))
                # )
                li._bindx.click(self.pyd_, pyro.pyd)
                with html.a(routerlink=('/pyro', {'pyd': pyro.pyd})):
                    html.span(pyro.pyd, Class='badge')
                    html.txt(' {name}')._fmt(
                        name=pyro.name_.do_action(lambda x: print('NAME:', x)))

    def render(self, node):
        with node.select('ul') as ul:
            ul._render(self.li_pyroes, self.pyroes_)


class AppComponent(Component):
    htmlsheet = '''
    <h1 class="title">AnPyLar Tourer</h1>
    <nav>
      <a routerLink="/pyroes" routerLinkActive="active">Pyroes</a>
    </nav>
    <router-outlet></router-outlet>
    '''


class AppModule(Module):
    components = AppComponent
    routes = [
        {
            'path': '',
            'redirect_to': '/pyroes',
            'path_match': 'full'
        },
        {
            'path': 'pyroes',
            'component': PyroesComponent,
        },
        {
            'path': 'pyro',
            'params': {'pyd': int},
            'component': PyroDetailComponent,
        }
    ]


if __name__ == '__main__':
    AppModule()
