$('.btt-link').click(function (e) {
    window.scrollTo(0, 0);
});

// Update quantity on click in bag
$('.update-link').click(function (e) {
    var form = $(this).prev('.update-form');
    form.submit();
});

// Remove item from the bag and reload on click
$('.remove-item').click(function (e) {
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/bag/remove/${itemId}/`;
    var data = {
        'csrfmiddlewaretoken': window.CSRF_TOKEN
    };
    $.post(url, data)
        .done(function () {
            location.reload();
        });
});