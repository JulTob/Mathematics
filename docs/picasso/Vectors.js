export class Vector {
    constructor(dx, dy) {
        this.dx = dx;
        this.dy = dy;
        }
  
    applyTo(point) {
        if (!(point instanceof Point)) {
            throw new Error("Expected a Point as argument");
            }
        return new Point(point.x + this.dx, point.y + this.dy);
        }
    }
