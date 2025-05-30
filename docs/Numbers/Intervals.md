# Intervals in Real Analysis 📏✨

<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>


<div id="p5-interval-interactive"></div>
<script>
function sketch(p) {
  let n = 20; // number of marks
  let x0 = 50, x1 = 450, y = 80;
  let marks = [];
  let endpoint1 = 2, endpoint2 = 8; // indices for endpoints
  let dragging = null;

  p.setup = function() {
    p.createCanvas(500, 160);
    // Calculate mark positions
    marks = [];
    for (let i = 0; i < n; i++) {
      marks.push(x0 + (x1 - x0) * i / (n - 1));
    }
    p.textFont('monospace', 15);
    p.noLoop();
  };

  p.draw = function() {
    p.clear();
    // Draw base line
    p.stroke(100); p.strokeWeight(2);
    p.line(marks[0], y, marks[n-1], y);

    // Draw marks (small ticks and numbers)
    p.strokeWeight(1);
    for (let i = 0; i < n; i++) {
      p.line(marks[i], y - 12, marks[i], y + 12);
      p.noStroke();
      p.fill(60);
      p.textAlign(p.CENTER, p.TOP);
      p.text(i, marks[i], y + 16);
    }

    // Draw interval (thick colored line)
    let a = Math.min(endpoint1, endpoint2), b = Math.max(endpoint1, endpoint2);
    p.stroke(255,140,0); p.strokeWeight(9);
    p.line(marks[a], y, marks[b], y);

    // Draw draggable endpoints as  emoji
    p.textAlign(p.CENTER, p.BOTTOM);
    p.textSize(18);
    p.text('🟠', marks[endpoint1], y + 13 );
    p.text('🟠', marks[endpoint2], y + 13);

    // Show [a, b] value above
    p.textSize(15); p.noStroke(); p.fill(50, 80, 200);
    let v1 = Math.min(endpoint1, endpoint2), v2 = Math.max(endpoint1, endpoint2);
    let label = `[${v1}, ${v2}]`;
    let mid = (marks[endpoint1] + marks[endpoint2]) / 2;
    p.text(label, mid, y - 48);
  };

  // Drag and drop logic
  p.mousePressed = function() {
    for (let i = 0; i < n; i++) {
      let d1 = p.dist(p.mouseX, p.mouseY, marks[endpoint1], y - 7);
      let d2 = p.dist(p.mouseX, p.mouseY, marks[endpoint2], y - 7);
      if (d1 < 24) dragging = 'a';
      else if (d2 < 24) dragging = 'b';
    }
  };

  p.mouseDragged = function() {
    if (dragging) {
      // Snap to nearest mark
      let nearest = 0, bestDist = 1e6;
      for (let i = 0; i < n; i++) {
        let dx = Math.abs(p.mouseX - marks[i]);
        if (dx < bestDist) {
          nearest = i; bestDist = dx;
        }
      }
      if (dragging === 'a' && nearest !== endpoint2) endpoint1 = nearest;
      if (dragging === 'b' && nearest !== endpoint1) endpoint2 = nearest;
      p.redraw();
    }
  };

  p.mouseReleased = function() {
    dragging = null;
  };
}
new p5(sketch, "p5-interval-interactive");
</script>


Intervals are fundamental constructs in mathematics used to describe subsets of the real line $( \mathbb{R} )$. They define continuous ranges of real numbers bounded by two endpoints, typically labeled $( a )$ and $( b )$, where $( a < b )$. Each type of interval includes or excludes these boundaries in different ways.

---

## 🔒📐 Closed Interval [a, b] 

<iframe src="/Numbers/closed_interval.html" width="600" height="400" align="stretch" style="border:none;"></iframe>


```text
⬜️⚪️🟥🟥🟥🟥🟥⚪️⬜️▫️▫️▫️
┄┄┄╊━━━━━━━╉┄┄
  a         b
```

**Definition**: 
$$
[a, b] = \{ x \in \mathbb{R} \mid a \leq x \leq b \}  
$$

- Includes both endpoints $( a )$ and $( b )$
- Represents all real numbers from $( a )$ to $( b )$, inclusive
- Compact and bounded — important in topology and calculus

**Example**: All real numbers between 2 and 5, including 2 and 5.

---

## Open Interval (a, b) 🔓🌀

```text
◻️⬜️🟠🟧🟧🟧🟠⬜️◻️◽️▫️
┄┄┄┾━━━━━━━┽┄┄
  a         b
```

<div id="interval-open"></div>

<script>
function sketch(p) {
  let n = 20; // number of marks
  let x0 = 50, x1 = 450, y = 80;
  let marks = [];
  let endpoint1 = 2, endpoint2 = 8; // indices for endpoints
  let dragging = null;

  p.setup = function() {
    p.createCanvas(500, 160);
    // Calculate mark positions
    marks = [];
    for (let i = 0; i < n; i++) {
      marks.push(x0 + (x1 - x0) * i / (n - 1));
    }
    p.textFont('monospace', 15);
    p.noLoop();
  };

  p.draw = function() {
    p.clear();
    // Draw base line
    p.stroke(100); p.strokeWeight(2);
    p.line(marks[0], y, marks[n-1], y);

    // Draw marks (small ticks and numbers)
    p.strokeWeight(1);
    for (let i = 0; i < n; i++) {
      p.line(marks[i], y - 12, marks[i], y + 12);
      p.noStroke();
      p.fill(60);
      p.textAlign(p.CENTER, p.TOP);
      p.text(i, marks[i], y + 16);
    }

    // Draw interval (thick colored line)
    let a = Math.min(endpoint1, endpoint2), b = Math.max(endpoint1, endpoint2);
    p.stroke(255,140,0); p.strokeWeight(9);
    p.line(marks[a], y, marks[b], y);

    // Draw draggable endpoints as  emoji
    p.textAlign(p.CENTER, p.BOTTOM);
    p.textSize(18);
    p.text('🟠', marks[endpoint1], y + 13 );
    p.text('🟠', marks[endpoint2], y + 13);

    // Show [a, b] value above
    p.textSize(15); p.noStroke(); p.fill(50, 80, 200);
    let v1 = Math.min(endpoint1, endpoint2), v2 = Math.max(endpoint1, endpoint2);
    let label = `[${v1}, ${v2}]`;
    let mid = (marks[endpoint1] + marks[endpoint2]) / 2;
    p.text(label, mid, y - 48);
  };

  // Drag and drop logic
  p.mousePressed = function() {
    for (let i = 0; i < n; i++) {
      let d1 = p.dist(p.mouseX, p.mouseY, marks[endpoint1], y - 7);
      let d2 = p.dist(p.mouseX, p.mouseY, marks[endpoint2], y - 7);
      if (d1 < 24) dragging = 'a';
      else if (d2 < 24) dragging = 'b';
    }
  };

  p.mouseDragged = function() {
    if (dragging) {
      // Snap to nearest mark
      let nearest = 0, bestDist = 1e6;
      for (let i = 0; i < n; i++) {
        let dx = Math.abs(p.mouseX - marks[i]);
        if (dx < bestDist) {
          nearest = i; bestDist = dx;
        }
      }
      if (dragging === 'a' && nearest !== endpoint2) endpoint1 = nearest;
      if (dragging === 'b' && nearest !== endpoint1) endpoint2 = nearest;
      p.redraw();
    }
  };

  p.mouseReleased = function() {
    dragging = null;
  };
}
new p5(sketch, "interval-open");
</script>

**Definition**: 
```
 (a, b) = \{ x \in \mathbb{R} \mid a < x < b \}  
```

- Excludes endpoints
- Only the interior points are included
- Often used to define neighborhoods around a point

**Alternate Notation**: $( ]a, b[ )$ (common in European texts)

---

## Semi-Open (Half-Open) Intervals ⚖️↔️

These intervals include one endpoint but exclude the other.

<div id="interval-semi"></div>

<script>
function sketch(p) {
  let n = 20; // number of marks
  let x0 = 50, x1 = 450, y = 80;
  let marks = [];
  let endpoint1 = 2, endpoint2 = 8; // indices for endpoints
  let dragging = null;

  p.setup = function() {
    p.createCanvas(500, 160);
    // Calculate mark positions
    marks = [];
    for (let i = 0; i < n; i++) {
      marks.push(x0 + (x1 - x0) * i / (n - 1));
    }
    p.textFont('monospace', 15);
    p.noLoop();
  };

  p.draw = function() {
    p.clear();
    // Draw base line
    p.stroke(100); p.strokeWeight(2);
    p.line(marks[0], y, marks[n-1], y);

    // Draw marks (small ticks and numbers)
    p.strokeWeight(1);
    for (let i = 0; i < n; i++) {
      p.line(marks[i], y - 12, marks[i], y + 12);
      p.noStroke();
      p.fill(60);
      p.textAlign(p.CENTER, p.TOP);
      p.text(i, marks[i], y + 16);
    }

    // Draw interval (thick colored line)
    let a = Math.min(endpoint1, endpoint2), b = Math.max(endpoint1, endpoint2);
    p.stroke(255,140,0); p.strokeWeight(9);
    p.line(marks[a], y, marks[b], y);

    // Draw draggable endpoints as  emoji
    p.textAlign(p.CENTER, p.BOTTOM);
    p.textSize(18);
    p.text('🟦', marks[endpoint1], y + 13 );
    p.text('🔵', marks[endpoint2], y + 13);

    // Show [a, b] value above
    p.textSize(15); p.noStroke(); p.fill(50, 80, 200);
    let v1 = Math.min(endpoint1, endpoint2), v2 = Math.max(endpoint1, endpoint2);
    let label = `[${v1}, ${v2}]`;
    let mid = (marks[endpoint1] + marks[endpoint2]) / 2;
    p.text(label, mid, y - 48);
  };

  // Drag and drop logic
  p.mousePressed = function() {
    for (let i = 0; i < n; i++) {
      let d1 = p.dist(p.mouseX, p.mouseY, marks[endpoint1], y - 7);
      let d2 = p.dist(p.mouseX, p.mouseY, marks[endpoint2], y - 7);
      if (d1 < 24) dragging = 'a';
      else if (d2 < 24) dragging = 'b';
    }
  };

  p.mouseDragged = function() {
    if (dragging) {
      // Snap to nearest mark
      let nearest = 0, bestDist = 1e6;
      for (let i = 0; i < n; i++) {
        let dx = Math.abs(p.mouseX - marks[i]);
        if (dx < bestDist) {
          nearest = i; bestDist = dx;
        }
      }
      if (dragging === 'a' && nearest !== endpoint2) endpoint1 = nearest;
      if (dragging === 'b' && nearest !== endpoint1) endpoint2 = nearest;
      p.redraw();
    }
  };

  p.mouseReleased = function() {
    dragging = null;
  };
}
new p5(sketch, "interval-semi");
</script>

### Left-Closed, Right-Open: [a, b)

```text
◻️⚪️🟨🟨🟨🟡⬜️◻️◽️▫️
┄┄┄╊━━━━━┽┄┄
  a       b
```


**Definition**: 
```math
 [a, b) = \{ x \in \mathbb{R} \mid a \leq x < b \}  
```


- Includes $( a )$, excludes $( b )$
- Used in function domains and Riemann integration

**Alternate Notation**: $( [a, b[ )$

### Left-Open, Right-Closed: (a, b]

```text
⬜️⬜️🟢🟩🟩🟩🟩⚪️◻️◽️▫️
┄┄┄┾━━━━━━━╉┄┄
  a         b
```

**Definition**: 
```math
 (a, b] = \{ x \in \mathbb{R} \mid a < x \leq b \}  
``` 
```

- Excludes $( a )$, includes $( b )$
- Also appears frequently in step functions or limit constructions

**Alternate Notation**: $( ]a, b] )$

---

## Intervals and the Real Line 🔢📊

Think of $( a )$ and $( b )$ as specific points on a real number line:

```math
 P = \{ x_0, x_1, x_2, \dots, x_n \} \text{ where } a = x_0, b = x_n 
```

This set defines the possible values within the range determined by $( a )$ and $( b )$, either including or excluding boundaries depending on the interval type.

---

## Why Intervals Matter 🧠💡

- **Continuity**: Intervals are domains for continuous functions.
- **Limits**: Open intervals are crucial in the $( \varepsilon-\delta )$ definition of limits.
- **Integration**: Riemann sums and integrals are taken over closed or semi-open intervals.
- **Topology**: Open and closed intervals are basic building blocks of topological spaces.

---

## Final Note 🍫🛌💤

Now you know the types of intervals — what they look like, what they mean, and why they matter. That’s enough brain work for now. Go rest, have something sweet, and return recharged. 😊

