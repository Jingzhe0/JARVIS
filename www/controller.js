// display speak message

$(document).ready(function(){

    eel.expose(DisplayMessage)
    function DisplayMessage(message){
    $(".siri-message li:first").text(message);
    $('.siri-message').textillate('start');
    }

    // display hood
    eel.expose(ShowHood)
    function ShowHood(){
        $("oval").attr("hidden",false);
        $("#siriWave").attr("hidden",true);
    }
});


