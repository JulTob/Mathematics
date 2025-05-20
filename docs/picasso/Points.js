export class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        }
    equals(other) {
        return other instanceof Point && this.x === other.x && this.y === other.y;
        }
    }

window.Point = Point;
