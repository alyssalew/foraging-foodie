"use strict";

function replaceLocation(results) {
    // console.log("Replace location");
    // $("input[name='inlineRadioOptions']:checked").val();

   $( "#location" ).val( $( "#inlineRadio-my-address.form-check-input:checked" ).val());
}


function enterLocation(results){
    // console.log ("Clicked into textbox");
    $( "#location" ).val('');
    $("#inlineRadio-my-address.form-check-input").prop('checked', false);
}

$( "#inlineRadio-my-address.form-check-input" ).on( "click", replaceLocation);

$( "#location" ).focus(enterLocation);