#!/usr/bin/node
const squareSize = parseInt(process.argv[2]);
if (Number.isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    let sqr = '';
    for (let j = 0; j < squareSize; j++) {
      sqr += 'X';
    }
    console.log(sqr);
  }
}
