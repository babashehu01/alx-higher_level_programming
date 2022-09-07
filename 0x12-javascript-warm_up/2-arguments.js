#!/usr/bin/node
// Script that prints a message depending of the number of arguments passed
const argV = process.argv.length;
if (argV == 2) {
	console.log('No arguement');
}
else if (argV == 3)
{
	console.log('Argument found');
}
else if (argV > 3) {
	console.log('Arguments dound');
}
else {
	console.log('No argument found');
}
