#!/usr/bin/node
function search () {
  args = [];
  for (let i = 0; i === i; i++) {
    if (parseInt(process.argv[i]) !== undefined) {
      args.push(parseInt(process.argv[i]));
    } else {
      break;
    }
  }
  if (!process.argv[2]) {
    console.log(0);
  } else {
    console.log(process.argv[2]);
  }
}

search()
