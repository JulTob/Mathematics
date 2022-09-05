// Processing

let x, y;
let num = 1;
let stepSize = 12;
let direction = 0;
let nSteps = 1;
let turner = 0;
//let isPrime = true;

function isPrime(value){
	if (value<2) return false;
	for (let i = 2; i*i <= value; i++){
		if(value % i == 0){
			return false;
			break;
		};
	}
	return true;
}

function setup() {
	createCanvas(1000, 1000);
	x= width / 2;
	y = height / 2;
	background(0);
}

function draw() {
	textSize(20);
	textAlign(CENTER,CENTER);
	fill(255);
	if(isPrime(num)){
		text("●", x, y); //text(num, x, y);
	} else {
		if (num == 1){text("○", x, y)}
		else{
		text("∙", x, y)};
	};
	
	switch(direction){
		case 0:
			x += stepSize; // Right
			break;
		case 1:
			y -= stepSize; // Up
			break;
		case 2:
			x -= stepSize; // Left
			break;
		case 3:
			y += stepSize // Down
			break;
	}
	

	if(num % nSteps == 0){
			direction = (direction + 1) %4;
			turner++;
		if(turner % 2 == 0){
		  nSteps++;
		}
	}
	num++;
	
	frameRate(20);
}
