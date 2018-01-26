;(function(){
    function add_overlay() {

        var elem = document.createElement('div');
        elem.id = 'anpylar-loading-overlay'
        elem.style.cssText = 'position: fixed; width: 100%; height: 100%;' + 'min-height: 100%;' +
            'left: 0;top: 0;background: rgba(224,224,224,0.33); z-index: 100000;'
        document.body.appendChild(elem);

        var elem4 = document.createElement('div');
        elem4.innerHTML = '<h1 style="text-align:center;position:relative;top:46%;transform:translateY(-46%);">Loading ...</h1>'
        elem4.style.cssText = 'position: fixed; width: 100%; height: 100%;' +
            'left: 0;top: 0; z-index: 10002;'
        elem.appendChild(elem4)

        var keyframes = '\
#anpylar-loading-wheel {\
  position: fixed;\
  top: 50%;\
  left: 50%;\
  width: 150px;\
  height: 150px;\
  margin: -75px 0 0 -75px;\
  border: 16px solid #f3f3f3;\
  border-radius: 50%;\
  border-top: 16px solid #3498db;\
  width: 120px;\
  height: 120px;\
  animation: spin 2s linear infinite;\
  z-index: 10001;\
}\
\
@keyframes spin {\
  0% { transform: rotate(0deg); }\
  100% { transform: rotate(360deg); }\
}';

        var elem2 = document.createElement('style');
        elem2.style.type = 'text/css'
        elem2.id = 'anpylar-loading-overlay-style'
        elem2.innerHTML = keyframes
        document.head.appendChild(elem2)

        var elem3 = document.createElement('div')
        elem3.id = 'anpylar-loading-wheel'
        elem.appendChild(elem3)
    }
    window.addEventListener('DOMContentLoaded', add_overlay, true)
})();
