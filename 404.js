var http = require("http");

http.createServer(function(req, res){

	if (req.url === "/") {
		fs.readFile("./public/index.html", "UTF-8", function(err, body){
			res.writeHead(200, {"Content-Type": 'text/html"});
			res.end(body);
