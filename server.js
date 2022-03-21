var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');



function Uptime(){
	uptime=os.uptime();
	days = Math.floor(uptime / 86400);
	hours = Math.floor(uptime % 86400 / 3600);
	minutes = Math.floor(uptime % 3600 / 600);
	seconds = Math.floor(uptime % 3600/60);
return `days:${days}, Hours:${hours}, Minutes:${minutes}, Seconds:${seconds}`;
}



var server = http.createServer(function(req, res){
	if (req.url === "/") {
	fs.readFile("./Public/index.html", "UTF-8", function(err, body){
	res.writeHead(200, {"Content-Type": "text/html"});
	res.end(body);
	});
}else if(req.url.match("/sysinfo")) {
	myHostName=os.hostname();
	totalMemory=((os.totalmem())/1048576);
	freeMemory=((os.freemem())/1048576);
	cpuCount=os.cpus().length;
	html=`
	<!DOCTYPE html>
	<html>
		<head>
		 <title>Node JS Response</title>
	</head>
	<body>
		<p>Hostname: ${myHostName}</p>
		<p>IP: ${ip.address()}</p>
		<p>Server Uptime: ${Uptime()} </p>
		<p>Total Memory:${totalMemory} </p>
		<p>Free Memory:${freeMemory} </p>
		<p>Number of CPUs:${cpuCount} </p>
		</body>
		</html>`
	
	res.writeHead(200, {"Content-Type": "text/html"});
	res.end(html);
}

	else{
		res.writeHead(404, {"Content-Type": "text/plain"});
		res.end(`404 File not Found at ${req.url}`);
	}
	

}).listen(3000)

console.log("Server listening on port 3000");