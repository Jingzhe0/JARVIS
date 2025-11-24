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
        eel.allCommand()()
        
    });


    function doc_keyUp(e) {
        // to test which key is down arror and ctrl at same time

        if(e.key === 'j' && e.metaKey) {
            eel.playAssistantSound()
            $("#oval").attr("hidden",true);
            $("#siriWave").attr("hidden",false);
            eel.allCommand()()
        }
    }

    document.addEventListener('keyup',doc_keyUp,false);


    function playAssistantSound (message) {  
        if (message !=""){
            $("#oval").attr("hidden",true);
            $("#siriWave").attr("hidden",false);
            eel.allCommand(message)
            $("#chatbox").val("")
            $("#micButton").attr("hidden",false);
            $("#SendBtn").attr("hidden",true);
        }
    }


    function ShowHideButton (message) {  
        if (message.length ==0){
            $("#micButton").attr("hidden",false);
            $("#SendBtn").attr("hidden",true);
        }
        else{
            $("#micButton").attr("hidden",true);
            $("#SendBtn").attr("hidden",false);
        }
            
    }


    $("#chatbox").keyup(function() {

        let message = $("#chatbox").val();
        ShowHideButton(message)
    });

    $("#SendBtn").click(function() {

        let message = $("#chatbox").val();
        playAssistantSound(message)
    });



     $("#chatbox").keypress(function(e) {

        key=e.which;
        if(e.key=="Enter"){
            let message = $("#chatbox").val();
            playAssistantSound(message)
        }
     });



});