console.log('hello world')

const socket = new WebSocket('ws://' + window.location.host + '/ws/indoomie-noodles/');

console.log(socket)

socket.onmessage = function(e){
    console.log('Server '+ e.data);
};

socket.onopen = function(e){
    socket.send(JSON.stringify({
        'message': 'hello from client',
    }));
}

