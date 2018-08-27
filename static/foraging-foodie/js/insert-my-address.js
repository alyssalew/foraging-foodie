"use strict";

function replaceLocation(results) {
    // console.log("Replace location");
    // $("input[name='inlineRadioOptions']:checked").val();

   $( "#location" ).val( $( "#inlineRadio-my-address:checked" ).val());
}


function enterLocation(results){
    // console.log ("Clicked into textbox");
    $( "#location" ).val('');
    $("#inlineRadio-my-address").prop('checked', false);
}

$( "#inlineRadio-my-address" ).on( "click", replaceLocation);

$( "#location" ).focus(enterLocation);