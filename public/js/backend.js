/*$(document).ready(function() {
    $("#submitButton").click(function() {
        $.ajax({
            type: "GET",
            url: "/v1/find",
            data: {
            },
            success: function(data) {
                
            }
        });
    });
});
*/

var call;
//var call = alert("This is the typeform API."); //checks for click submit
$(document).ready(function() {
    //$(".button-wrapper submit").click(function() {
        httpGetAsync('https://api.typeform.com/v1/form/z5pYTY?key=4b169802839212949e0bd45b7872426972fe2db3', call);
    //});
});

$(document).ready(function() {
    $(".button-wrapper submit").click(function() {
        httpGetAsync('https://api.typeform.com/v1/form/z5pYTY?key=4b169802839212949e0bd45b7872426972fe2db3', call);
        $(location).attr('href', 'file:///home/inandi2015/lyft4humanity/templates/success.html')
    });
});

function httpGetAsync(theUrl, callback)
{   
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            //callback(xmlHttp.responseText);
            console.log(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
    //console.log(xmlHttp.responseText);
}