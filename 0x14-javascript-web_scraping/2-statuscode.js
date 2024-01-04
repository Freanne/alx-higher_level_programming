#!/usr/bin/node

const request = require('request');


const urlPath = process.argv[2]

request.get(urlPath, (error, response ) => {
	if (error){
		console.error(error)
	}
	else {
		console.log(response.status)
	}
});
