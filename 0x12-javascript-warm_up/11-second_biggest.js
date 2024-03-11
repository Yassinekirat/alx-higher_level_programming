#!/usr/bin/node
if ((isNaN(process.argv[2])) || (process.argv.length === 3)) {
  console.log('0');
} else {
  const integers = process.argv.slice(2).map(Number).filter(Number.isInteger).sort((a, b) => a - b);
  console.log(integers[integers.length - 2]);
}
