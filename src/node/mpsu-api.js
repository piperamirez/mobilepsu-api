var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('mpsu-db.sqlite');
 
var express = require('express');
var restapi = express();

restapi.all('*', function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
 });

restapi.get('/data', function(req, res){
	var data = [];
	db.each("QUERY", function(err, row) {
		data.push({
			"attribute" : row.attribute,
		});
    }, function() {
    	res.json(data);
    });
});
  
restapi.listen(3000);
