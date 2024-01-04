#!/usr/bin/node

const fs =  require('fs')

const filePath = process.argv[2]

const printIn = process.argv[3]

fs.writeFile(filePath, printIn, "utf-8", (err, data) => {
	if(err){
		console.error(err)
	}
	else{
		console.log(data)
	}
});
