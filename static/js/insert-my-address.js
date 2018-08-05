function replaceLocation(results) {
    // console.log(results)
    // $("input[name='inlineRadioOptions']:checked").val();

   $( "#location" ).val( $( "input:checked" ).val());
}


$( "input" ).on( "click", replaceLocation);