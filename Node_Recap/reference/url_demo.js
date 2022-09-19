const url = require('url');

const myUrl = new URL('http://mywebsite.com/hello.html?id=100&status=active')
console.log(myUrl.href); //.host, .hostname, .toString(), pathname, search, searchParams