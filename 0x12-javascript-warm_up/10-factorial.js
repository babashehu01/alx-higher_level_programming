#!/usr/bin/node
const number = parseInt(process.argv[2]);
let cursed = 1;
function curse () {
  if (Number.isNaN(number)) {
    console.log(1);
  } else {
    for (let i = number; i >= 1; i--) {
      cursed *= i;
    }
    console.log(cursed);
  }
}

curse();
