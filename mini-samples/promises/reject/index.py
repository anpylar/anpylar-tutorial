from anpylar import Promise, call_delayed


def executor(resolve, reject):
    # call_delayed(1000, lambda: reject(Exception('Blistering Barnacles!')))
    call_delayed(1000, lambda: reject('Blistering barnacles!'))


mypromise = Promise(executor) \
                .then(lambda x: x * 2) \
                .then(lambda x: x * 3) \
                .then(print) \
                .catch(lambda x: print('Error:', x))
