// VectorSpace.js

if (!window.Point || !window.Vector) {
    throw new Error("Point and Vector must be loaded before VectorSpace");
    }

class VectorSpace {
    static apply(v, p) {
        if (!(v instanceof Vector) || !(p instanceof Point)) {
            throw new Error("Expected a Vector and a Point");
            }
        return new Point(p.x + v.dx, p.y + v.dy);
        }

  static subtract(p1, p2) {
      if (!(p1 instanceof Point) || !(p2 instanceof Point)) {
          throw new Error("Expected two Points");
          }
      return new Vector(p1.x - p2.x, p1.y - p2.y);
      }
  }

window.VectorSpace = VectorSpace;
