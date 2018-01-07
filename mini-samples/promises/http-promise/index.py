from anpylar import Http

Http().get('http://127.0.0.1:2223/index.html') \
    .to_promise() \
    .then(lambda x: print('Promise.then:', x)) \
    .catch(lambda x: print('Promise.catch: Error happened', x))
