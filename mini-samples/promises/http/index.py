from anpylar import Promise, Http, HttpException


def executor(resolve, reject):
    def _resolver(resp):
        resolve(resp[0:min(50, len(resp))])  # 1st 50 chars of the answer

    def _rejecter(error):
        reject(error)

    Http().get('http://127.0.0.1:2223/index.html') \
        .catch_exception(lambda x: None if _rejecter(x) else None) \
        .filter(lambda x: x is not None) \
        .subscribe(_resolver)


Promise(executor) \
    .then(lambda x: print('Promise.then:', x)) \
    .catch(lambda x: print('Promise.catch: Error happened', x))
