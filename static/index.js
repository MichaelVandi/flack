document.addEventListener('DOMContentLoaded', ()=>{

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    var channelName_;
    // Function to create channel
    document.querySelector('#create').onclick = function createChannel(){
        //Making the prompt alert stay a little longer
        var channelName = prompt("Enter the channel Name");
        // If channel name is empty
        if(channelName===""){
            alert ("Channel name cannot be empty");
        }
        else{
            // Send the data to flask server
            channelName_=channelName;
            socket.emit('create channel', {'name': channelName});
        }
    }

    // Alert the feedback received from create channel broadcast
    socket.on('create feedback', data =>{

        switch(data.status){
            case 1:
                const li = document.createElement('li');
                li.innerHTML = `#${channelName_}`;
                document.querySelector('#channels').append(li);
                alert (data.message);
                break;
            default:
                alert (data.message);
                break


        }
    })
    



});