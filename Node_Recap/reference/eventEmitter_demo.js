const EventEmiiter = require('events');

class MyEmitter extends EventEmiiter{}

//Init object
const myEmmiter = new MyEmitter();

//Event Listener
myEmmiter.on('event', () => console.log('Event Fired'));

//Init Event
myEmmiter.emit('event');
myEmmiter.emit('event');
myEmmiter.emit('event');