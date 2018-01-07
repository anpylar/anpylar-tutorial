from anpylar import Promise, call_delayed


def executor(resolve, reject):
    call_delayed(1000, lambda: resolve(1))


mypromise = Promise(executor) \
                .then(lambda x: x * 2) \
                .then(lambda x: x * 3) \
                .then(print) \
                .catch(lambda x: print('Error:', x))
