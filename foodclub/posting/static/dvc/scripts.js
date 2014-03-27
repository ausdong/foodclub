$(document).ready(function(){
    $('.intro').hide();
    $('#begin_button').mouseenter(function(){
        $('.intro').slideDown();
    });


    $('#begin_button').mouseleave(function(){
        $('.intro').hide();
    });


});
