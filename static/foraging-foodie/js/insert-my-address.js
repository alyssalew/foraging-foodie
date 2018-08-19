"use strict";

function replaceLocation(results) {
    // console.log("Replace location");
    // $("input[name='inlineRadioOptions']:checked").val();

   $( "#location" ).val( $( ".form-check-input:checked" ).val());
}


function enterLocation(results){
    // console.log ("Clicked into textbox");
    $( "#location" ).val('');
    $(".form-check-input").prop('checked', false);
}

$( ".form-check-input" ).on( "click", replaceLocation);

$( "#location" ).focus(enterLocation);