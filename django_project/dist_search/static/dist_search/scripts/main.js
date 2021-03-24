$.fn.extend({
    toggleText: function(a, b){
        return this.text(this.text() == b ? a : b);
    }
});

$('#distance-button').click(function() {
    $('.distance-measurement').toggleClass(' show ')
    $('#distance-button').toggleText('Display distance', 'Hide distance')
    console.log("Hej")
})