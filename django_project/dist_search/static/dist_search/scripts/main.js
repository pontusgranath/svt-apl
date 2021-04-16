try {
    const queryString = window.location.search
    const urlParams = new URLSearchParams(queryString);
    const currentInlineSearch = urlParams.get('inline-search-title')
    console.log(queryString)
    console.log(currentInlineSearch)

    $(document).ready(function(){
        window.location.href = '#' + currentInlineSearch
    })
}
catch {}

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

