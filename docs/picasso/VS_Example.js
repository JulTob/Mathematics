// vectorSpaceExample.js

(function () {
  const sketch = (p) => {
    let t = 0;
    let origin = new Point(100, -100);
    let direction = new Vector(200, 100);
    let target = VectorSpace.apply(direction, origin);

    p.setup = () => {
      const canvas = p.createCanvas(400, 400);
      canvas.parent("vectorSpaceCanvas");
    };

    p.draw = () => {
      p.background(255);
      p.translate(p.width / 2, p.height / 2);
      p.stroke(0);
      p.line(-p.width / 2, 0, p.width / 2, 0);
      p.line(0, -p.height / 2, 0, p.height / 2);

      // draw vector from origin to target
      p.stroke(0, 0, 255);
      p.line(origin.x, -origin.y, target.x, -target.y);

      // animate a point along the vector
      let pt = new Point(
        origin.x + direction.dx * t,
        origin.y + direction.dy * t
      );
      p.fill(255, 0, 0);
      p.circle(pt.x, -pt.y, 10);

      t += 0.01;
      if (t > 1) t = 1;
    };
  };

  new p5(sketch, 'vectorSpaceCanvas');
})();
