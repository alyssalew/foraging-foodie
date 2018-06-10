"use strict";

function showRestaurantInfo (results){
    console.dir(results);
    console.log("Showing more info");
    // alert("More info: " + results['photos']);

    // $('collapseExample'+results['id']).append("thing");

}

function getRestaurantInfo (evt) {
    var inputs = {
       // "biz_id" : "Qfc4w5l92Uvq9BsrP15O4A"
       "biz_id": $('#my_button').val() // This only works with "1st my_button"
    };

    $.get('/more-info.json', inputs, showRestaurantInfo);
}


$('#my_button').on('click', getRestaurantInfo);