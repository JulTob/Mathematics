// Initialize the equation sides
const b = Math.floor(Math.random() * 25);
let leftSide = `x + ${b}`;
let rightSide = '0';

window.onload = function() {
  generateRandomEquation();
  document.getElementById('submitBtn').addEventListener('click', applyOperation);
  document.getElementById('undoBtn').addEventListener('click', reset);
};


function updateDisplay() {
  const beautify = expr =>
    expr
      .replace(/\*/g, '·')   // Replace * with ·
      .replace(/\//g, ':');  // Replace / with :

  const equation = `${beautify(leftSide)} = ${beautify(rightSide)}`;
  document.getElementById('mathDisplay').innerHTML = `\\(${equation}\\)`;
  MathJax.typeset(); // Render the equation using MathJax
  }

// Function to reset the equation to its initial state
function reset() {
  generateRandomEquation();
  document.getElementById('feedback').textContent = '';
}

// Initialize the display when the page loads
window.onload = function() {
    updateDisplay();
    document.getElementById('submitBtn').addEventListener('click', applyOperation);
    document.getElementById('undoBtn').addEventListener('click', reset);
  };

function applyOperation() {
  const operation = document.getElementById('operationSelector').value;
  const number = document.getElementById('numberSelector').value;

  if (number === '') {
    document.getElementById('feedback').textContent = 'Please enter a number.';
    return;
  }
    if (operation === '÷' && Number(number) === 0) {
      document.getElementById('feedback').textContent = '⚠️ Stop! Division by zero is forbidden!';
      return;
    }
  try {
    // Construct new expressions by appending the operation
    leftSide = `(${leftSide}) ${operation} ${number}`;
    rightSide = `(${rightSide}) ${operation} ${number}`;

    // Simplify the expressions
    leftSide = math.simplify(leftSide).toString();
    rightSide = math.simplify(rightSide).toString();

    updateDisplay();
    document.getElementById('feedback').textContent = '';
  } catch (err) {
    console.error(err);
    document.getElementById('feedback').textContent = 'Invalid move!';
  }
}

function generateRandomEquation() {
  const getRandom = () => Math.floor(Math.random() * 25) - 12; // -12 to 12

  let a = 0;
  while (a === 0) a = getRandom(); // No zero for 'a'
  const b = getRandom();
  const c = getRandom();

  leftSide = `${a}x + ${b}`;
  rightSide = `${c}`;

  updateDisplay();
}

function applyOperation() {
  const operation = document.getElementById('operationSelector').value;
  const number = document.getElementById('numberSelector').value;

  if (number === '') {
    document.getElementById('feedback').textContent = 'Please enter a number.';
    return;
  }

  if (operation === '/' && Number(number) === 0) {
    document.getElementById('feedback').textContent = '🚫➗0️⃣';
    return;
  }

  // Show the operation visually
  const opSymbol = operation === '*' ? '·' : operation === '/' ? ':' : operation;
  const overlay = document.getElementById('operationOverlay');
  overlay.textContent = `${opSymbol}${number}`;
  overlay.style.visibility = 'visible';
  overlay.style.opacity = 0;



  
  // Animate it
  anime({
    targets: '#operationOverlay',
    opacity: [0, 1],
    duration: 300,
    easing: 'easeInOutQuad',
    complete: () => {
      // Apply the operation AFTER animation
      try {
        leftSide = `(${leftSide}) ${operation} ${number}`;
        rightSide = `(${rightSide}) ${operation} ${number}`;

        leftSide = math.simplify(leftSide).toString();
        rightSide = math.simplify(rightSide).toString();

        updateDisplay();
        document.getElementById('feedback').textContent = '';
      } catch (err) {
        document.getElementById('feedback').textContent = '⛔️';
      }

      // Fade out the overlay
      anime({
        targets: '#operationOverlay',
        opacity: [1, 0],
        duration: 600,
        easing: 'easeInOutQuad',
        complete: () => {
          overlay.style.visibility = 'hidden';
        }
      });
      
    }
  });
  anime({
  targets: '#mathDisplay',
  opacity: [1, 0],
  duration: 400,
  easing: 'easeInOutQuad',
  complete: function() {
    updateDisplay(); // This refreshes with the new, correct equation!
    anime({
      targets: '#mathDisplay',
      opacity: [0, 1],
      duration: 200,
      easing: 'easeInOutQuad'
    });
  }
});

}