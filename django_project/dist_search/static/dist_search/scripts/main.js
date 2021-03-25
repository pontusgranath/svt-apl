$('#distance-button').click(function() {
    $('.distance-measurement').toggleClass(' show ')

    if ($('#distance-button').hasClass('activated')) {
        $('#distance-button').text = 'Display distance'
    }
    else {
        $('#distance-button').text = 'Hide distance'
    }
})

