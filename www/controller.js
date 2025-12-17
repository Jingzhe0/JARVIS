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
        $("#oval").attr("hidden",false);
        $("#siriWave").attr("hidden",true);
    }



    // chat panel on right
    eel.expose(senderText)
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-end mb-4">
            <div class = "width-size">
            <div class="sender_message">${message}</div>
        </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    eel.expose(receiverText)
    function receiverText(message) {

        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-start mb-4">
            <div class = "width-size">
            <div class="receiver_message">${message}</div>
            </div>
        </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
        
    }

    

    // Hide Loader and display Face Auth animation
    eel.expose(hideLoader)
    function hideLoader() {

        $("#Loader").attr("hidden", true);
        $("#FaceAuth").attr("hidden", false);

    }
    // Hide Face auth and display Face Auth success animation
    eel.expose(hideFaceAuth)
    function hideFaceAuth() {

        $("#FaceAuth").attr("hidden", true);
        $("#FaceAuthSuccess").attr("hidden", false);

    }
    // Hide success and display 
    eel.expose(hideFaceAuthSuccess)
    function hideFaceAuthSuccess() {

        $("#FaceAuthSuccess").attr("hidden", true);
        $("#HelloGreet").attr("hidden", false);

    }


    // Hide Start Page and display blob
    eel.expose(hideStart)
    function hideStart() {

        $("#Start").attr("hidden", true);

        setTimeout(function () {
            $("#oval").addClass("animate__animated animate__zoomIn");

        }, 1000)
        setTimeout(function () {
            $("#oval").attr("hidden", false);
        }, 1000)
    }


    let gestureOn = false;

    
    function toggleGesture() {
    if (!gestureOn) {
        eel.ui_start_gesture()(function (res) {
            if (res) {
                gestureOn = true;
                document.getElementById("gestureBtn").innerText = "🖐️ Gesture ON";
            }
        });
    } else {
        eel.ui_stop_gesture()(function (res) {
            if (res) {
                gestureOn = false;
                document.getElementById("gestureBtn").innerText = "🖐️ Gesture OFF";
            }
        });
    }
}




});


