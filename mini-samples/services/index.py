from anpylar import Component, Module


class MyService:
    count = 0

    def next_count(self):
        self.count += 1
        return self.count


class MyComponent(Component):
    htmlsheet = '''
    <h2 [counter_]>The count is {}</h2>
    <button (click)="countup()">Count</button>
    '''

    bindings = {'counter': 0}

    def countup(self):
        self.counter_(self.myservice.next_count())


class MyModule(Module):
    services = {'myservice': MyService}

    components = MyComponent


MyModule()
