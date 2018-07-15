var http = require('http');


http.createServer(function(request,response){


    response.writeHead(200,{'Content-Type':'text/html'});
	
	response.end('<h1>hello world</h1>');
}).listen(8080);

console.log('Server running at http://localhost:8080/');
