export class Vector {
    constructor(dx, dy) {
        this.dx = dx;
        this.dy = dy;
        }

    add(other) {
        if (!(other instanceof Vector)) throw new Error("Expected Vector");
        return new Vector(this.dx + other.dx, this.dy + other.dy);
        }
    
    scale(scalar) {
        return new Vector(this.dx * scalar, this.dy * scalar);
        }


    applyTo(point) {
        if (!(point instanceof Point)) {
            throw new Error("Expected a Point as argument");
            }
        return new Point(point.x + this.dx, point.y + this.dy);
        }
    }

window.Vector = Vector;
