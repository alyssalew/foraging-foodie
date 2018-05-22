"use strict";

function showRestaurantInfo (results){
    console.dir(results);
    console.log("Showing more info");
    alert("More info:" + results);

}

function getRestaurantInfo (evt) {
    var inputs = {
       "biz_id" : "Qfc4w5l92Uvq9BsrP15O4A"
       // $('.btn btn-info').val()
    };

    $.get('/more-info.json', inputs, showRestaurantInfo);
}


$('#my_button').on('click', getRestaurantInfo);