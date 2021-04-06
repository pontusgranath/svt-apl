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

$('.list-title').click(function search(bool){
    try {
    let searchedTitle = $(this).attr("show-title")
    console.log(searchedTitle) // DEBUG // DEBUG // DEBUG

    $('.inline-search-results').remove()
    $(this).append("<div class='inline-search-results py-2 px-4'><h3>Search results for: <span>"+ searchedTitle +"</span></h3><ul><li>Titel 1</li><li>2 Titel</li><li>Titel 3</li><li>4 Titel</li><li>Titel 5</li></ul></div>")
    }
    catch (ReferenceError) {
        // skip ???
        console.log("ReferenceError")
    }
})