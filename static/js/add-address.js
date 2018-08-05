"use strict";


function showAddressResults(results) {
    // console.log(results);
    var address_obj = results[0];

    alert("You have addded a new address! \n" + address_obj['label'] + ": " + address_obj['address']);
    
    // $('.dynamic').append(results);

    $("#new-address").html(address_obj['label']+ ' -- ' + address_obj['address'])

}

function submitAddress(evt) {
    evt.preventDefault();

    var formInputs = {
        "label": $("#inputLabel").val(),
        "address1": $("#inputAddress").val(),
        "city": $("#inputCity").val(),
        "state": $("#inputState").val(),
        "zipcode": $("#inputZip").val(),
    };

    $.post('/new-address', formInputs, showAddressResults);
}

$("#new-address-form").on("submit", submitAddress);