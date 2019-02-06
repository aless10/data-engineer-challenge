var loadingAnimation = '<div id="animated" class="preloader-wrapper small active">\
                            <div class="spinner-layer spinner-green-only">\
                              <div class="circle-clipper left">\
                                <div class="circle"></div>\
                              </div><div class="gap-patch">\
                                <div class="circle"></div>\
                              </div><div class="circle-clipper right">\
                                <div class="circle"></div>\
                              </div>\
                            </div>\
                          </div>';
function animateLoad (element) {
    element.innerHTML = loadingAnimation;
}

$(document).on('click', '.animate-button', function(e) {
    animateLoad(this);
})
