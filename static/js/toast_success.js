$(document).ready(function () {
    $('.toast').toast('show');
    setTimeout(function () {
        $('.toast').toast('hide');
    }, 5000);
});