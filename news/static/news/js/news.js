$('#new-image').change(function () {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});

/** Button to go to top of the page */
$('.btt-link').click(function (e) {
    window.scrollTo(0, 0);
});