var angle = 0;
var slider;

function setup() {
	createCanvas(400, 400);
	slider = createSlider(0, TWO_PI, PI/4, PI/360);
	}

function draw() {
	background(0);
  
  	angle = slider.value();
	
	// Change origin to ground
	translate(200, height);
	branch(100, 255)	
	}

function branch(len, st) {
	stroke(st)
	line(0, 0, 0, -len);
	translate(0, -len);
  	if (len>0.5) {
    	push(); // Time Save
      		rotate(angle);
      		branch(len*0.6, st-20);
    	pop();  // Back Time
    	push();
      		rotate(-angle);
      		branch(len*0.5, st-20);
    	pop();
  		}
	}
