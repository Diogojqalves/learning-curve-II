/*const Logger = require('./logger');
const logger = new Logger();

logger.on('message', (data) => console.log('Called Listener:', data));


logger.log('Hello World');




const Person = require('./person');

const somePerson = new Person('Me', 25);
somePerson.greeting();
*/
const http = require('http');
const path = require('path');
const fs = require('fs');

const server = http.createServer((req, res) => {
  /*  if(req.url === '/') {
        fs.readFile(path.join(__dirname, 'public', 'index.html'), (err, data) => {
            if(err) throw err;
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.end(data) //nodemon listens to the changes -> npm run dev    
        })
    };
    if(req.url === '/api/users') {
        const users = [
            {name: 'Bob', age: 40},
            {name: 'Doe', age: 40}
        ];
        res.writeHead(200, {'Content-Type': 'application/json'});
        res.end(JSON.stringify(users));
    }
    */
   //File path
    let filePath = path.join(__dirname, 'public', req.url === '/' ? 'index.html' : req.url);
    //Extension of file
    let extname = path.extname(filePath);
    //Initial content type
    let contentType = 'text/html';
    //check ext and set content type
    switch(extname) {
        case '.js':
            contentType = 'text/javascript';
            break;
        case '.css':
            contentType = 'text/css';
            break;
        case '.json':
            contentType = 'application/json';
            break;
        case '.png':
            contentType = 'image/png';
            break;
    }

    //read file
    fs.readFile(filePath, (err, content) => {
        if(err) {
            if(err.code === 'ENOENT') {
                //PAGE NOT FOUND
                fs.readFile(path.join(__dirname, 'public', '404.html'), (err, data) => {
                    res.writeHead(200, {'Content-Type': 'text/html'});
                    res.end(data, 'utf8');
                })
            } else {
                //some server error
                res.writeHead(500);
                res.end(`Server Error: ${err.code}`);
            }
        } else {
            //success
            res.writeHead(200, {'Content-Type': contentType})
            res.end(content, 'utf8');
        }
    });
});
const PORT = process.env.PORT || 5000;
server.listen(PORT, () => console.log(`Server running on port ${PORT}`));
