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

// Creates inline search container on click
$('.list-title').click(function search(bool){
    try {
    let searchedTitle = $(this).attr("show-title")
    console.log(searchedTitle) // DEBUG // DEBUG // DEBUG

    $('.inline-search-wrapper').remove()
    $("body").append("<div class='inline-search-wrapper'><div class='inline-search-results py-2 px-4'><h3>Search results for: <span>"+ searchedTitle +"</span></h3><ul><li>Titel 1</li><li>2 Titel</li><li>Titel 3</li><li>4 Titel</li><li>Titel 5</li></ul></div></div>")
    }
    catch (ReferenceError) {
        // skip ???
        console.log("ReferenceError")
    }
})

// Removes inline search container if mouse is clicked outside of it
$(document).mouseup(function(e) 
{
    var container = $(".inline-search-results")

    // If the target of the click isn't the container nor a descendant of the container
    if (!container.is(e.target) && container.has(e.target).length === 0) 
    {
        $('.inline-search-wrapper').remove()
    }
});