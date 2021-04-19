// Scrolls down to selected title on pageload
try {
    const queryString = window.location.search
    const urlParams = new URLSearchParams(queryString);
    const currentInlineSearch = urlParams.get('inline-search-title')

    $(document).ready(function() {
        window.location.href = '#' + currentInlineSearch
    })
}
catch {}

let distanceButtonText = $('#distance-button').text()

// Toggles text and border on toggle distance button
$('#distance-button').click(function() {
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
