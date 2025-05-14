function setup() {
  createCanvas(400, 300);
}

function draw() {
  background(220);
  circle(mouseX, mouseY, 50);

  let xLabel = document.getElementById('x-label');
  xLabel.innerText = 'X: ' + mouseX;

  let yLabel = document.getElementById('y-label');
  yLabel.innerText = 'Y: ' + mouseY;
}
