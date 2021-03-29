let distanceButtonText = $('#distance-button').text()

$('#distance-button').click(function () {
    $('.distance-measurement').toggleClass(' show ')


    if ($('#distance-button').hasClass('activated')) {
        $('#distance-button').text(distanceButtonText)
        $('#distance-button').removeClass(' activated ')
    }
    else {
        $('#distance-button').text('Hide distance')
        $('#distance-button').addClass(' activated ')
    }
})

$(document).on('click', '.list-title', function() {    
    $.ajax({
        // url: '/calculate_distance',
        method: 'POST', // or another (GET), whatever you need
        data: {
            // csrfmiddlewaretoken: "{{ csrf_token }}",
            name: 'inline-search', // data you need to pass to your function
            click: true
        },
        success: function (data) {
            console.log('llama')
            // success callback
            // you can process data returned by function from views.py
        }
    });
});
