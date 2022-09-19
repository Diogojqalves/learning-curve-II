const EventEmiiter = require('events');
const uuid = require('uuid'); //npm install v4, generates an id


class Logger extends EventEmiiter{
    log(msg) {
        //call event
        this.emit('message', {id: uuid.v4(), msg});
    }
}

module.exports = Logger;