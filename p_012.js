function* fibonacci() { // a generator function
  let counter = 0;
  let tringular = counter
  while (true){
    counter += 1
    tringular += counter
    yield tringular
  }
}

function div_counter(n){
  let divs = 1
  for (let j=1; j<=Math.floor(n/2) ;j++){
    if (n % j == 0){
      divs += 1
    }
  }
  return divs
}

for (let n of fibonacci()) {
  
  // truncate the sequence at 1000
  if (div_counter(n) >= 500) {
    console.log(n);
    break;
  }
}