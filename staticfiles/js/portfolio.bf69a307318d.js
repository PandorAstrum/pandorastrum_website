//portfolio page re build
var $portfolio = document.querySelector('.portfolio');
var $elementsArr = [].slice.call(document.querySelectorAll('.p-el'));
var $clsBtnArr = [].slice.call(document.querySelectorAll('.p-el-close-btn'));

setTimeout(function() {
    $portfolio.classList.remove('p-inactive');
}, 200);

$elementsArr.forEach(function($el) {
    $el.addEventListener('click', function() {
        if (this.classList.contains('p-active')) return;
        $portfolio.classList.add('p-el-active');
        this.classList.add('p-active');
    });
});

$clsBtnArr.forEach(function($btn) {
    $btn.addEventListener('click', function(e) {
        e.stopPropagation();
        $portfolio.classList.remove('p-el-active');
        document.querySelector('.p-el.p-active').classList.remove('p-active');
    });
});
