#!/usr/bin/node
const argV = process.argv.length;
if (argV == 2) {
	console.log('No argument');
}
else if (argV == 3)
{
	console.log('Argument found');
}
else if (argV > 3) {
	console.log('Arguments found');
}
else {
	console.log('No argument found');
}
