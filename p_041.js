function is_prime(x){
	if (x <= 1){
		return false;
	}
	else if (x <= 3){
		return true;
	}
	else if (x % 2 == 0){
		return false;
		}
	else{
		for (var i=3; i <= Math.ceil(Math.sqrt(x)) + 1; i+=2){
			if (x % i == 0){
				return false;
			}
		}
		return true;
	}
}

function is_pandigital(num){
	return num.length == new Set(num).size;
}

function compute_answer(){
	for (var i=1000000000; i <= 20000000000; i++){
		if (is_pandigital(String(i))){
			console.log(i);

			if (is_prime(i)){
				
				console.log("ans : ", i);
				break;
				return;
			}
		}
	}
}

compute_answer()

// function F(num){
// 	// # ans = 0
// 	// # for num in range(1, lim):
// 	for (let i=2;  i <= Math.ceil(Math.sqrt(num)) + 1; i++){
// 		for (let j=2; j <= Math.ceil(num**0.33333) + 1; j++){
// 			if (((i**2) * (j**3)) == num) return true
// 		}
// 	}
// 	return false
// }

// var ans = 0
// for (let i=20000; i <=3000000 ; i++){
// 	if (is_prime(i)) continue
// 	if (F(i)) ans += 1
// 	console.log(i)
// }
// // # F(9*(10**18))
// console.log(ans+130)