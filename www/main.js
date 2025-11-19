$(document).ready(function () {
    
    $('.text').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"bounceIn",
        },
        out:{
            effect:"bounceOut",
        },
    });

    // siri configuration

    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitute:"1",
    speed:"0.10",
    autostart:true
  });


//   siri message animation

 $('.siri-message').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"fadeInUp",
            sync:true,
        },
        out:{
            effect:"fadeOutUp",
            sync:true,
        },
    });


    // mic button siri wave

    $("#micButton").click(function () { 
        eel.playAssistantSound()
        $("#oval").attr("hidden",true);
        $("#siriWave").attr("hidden",false);
        eel.takecommand()()
        
    });

});