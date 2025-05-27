from math import pow
from math import isclose

def algebraic(val):
    if isinstance(val, Expr):
        return val
    return Constant(val)
    
def numeric_value(x):
    while isinstance(x, Constant):
        x = x.value
    return x

class Expr:
    def simplify(self):
        return self

    def __add__(self, other):
        return Add(self, algebraic(other)).simplify()
    def __radd__(self, other):
        return Add(algebraic(other), self).simplify()
        
    def __mul__(self, other):
        return Mul(self, algebraic(other)).simplify()
    def __rmul__(self, other):
        return Mul(algebraic(other), self).simplify()
        
    def __sub__(self, other):
        return Add(self, Neg(algebraic(other))).simplify()
    def __rsub__(self, other):
        return Add(algebraic(other), Neg(self)).simplify()
        
    def __truediv__(self, other):
        return Div(self, algebraic(other)).simplify()
    def __rtruediv__(self, other):
        return Div(algebraic(other), self).simplify()
        
    def __neg__(self):
        return Neg(self).simplify()
        
    def __pow__(self, exponent):
        return Pow(self, algebraic(exponent)).simplify()
    def __rpow__(self, base):
        return Pow(algebraic(base), self).simplify()
        
    def evaluate(self, env={}):
        raise NotImplementedError("Evaluation not implemented for this type")
    def substitute(self, var_name: str, replacement: "Expr"):
        """Return a copy where every occurrence of Variable(var_name)
        is replaced by the expression `replacement`."""
        raise NotImplementedError

# Leafs
def Var(Expr):
    return Variable(Expr)

class Variable(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def evaluate(self, env={}):
        return env.get(self.name, 0)
    def substitute(self, var_name, replacement):
        return replacement if self.name == var_name else self

def Cons(Expr):
    return Constant(Expr)
    
class Constant(Expr):
    def __init__(self, value, img=None):
        if isinstance(value, Constant): 
            self.value = Constant(value.value)
        else: self.value = value
       # self.imaginary = img

    def __str__(self):
        #if self.imaginary == None:
            return str(self.value)
        #else:
        #    return str(self.value) + "+" + str(self.imaginary) + "𝚒"

    def evaluate(self, env={}):
        return self.value
        
    def substitute(self, var_name, replacement):
        return self          # constants are unaffected
 
pi = Variable("π")
euler = Variable("e")
im = Variable("i")
    
# Nodals
class Add(Expr):
    def __init__(self, *terms):
        self.terms = list(terms)
    def simplify(self):
        # 1) Flatten and simplify children
        flat = []
        for t in self.terms:
            t = t.simplify()
            if isinstance(t, Add):
                flat.extend(t.terms)
            else:
                flat.append(t)

        # 2) Bucket by monomial key
        buckets = {}   # monomial_key -> coeff
        others  = []   # non-polynomial terms

        def monomial_key(term):
            """
            Return (key, coeff) if term is coeff * x1^p1 * x2^p2 * …,
            else (None, term).
            Handles leading Neg(...) by applying sign.
            """
            # 1) Pull off any Neg() wrappers
            sign = 1
            while isinstance(term, Neg):
                sign *= -1
                term = term.term
        
            # 2) Pure constant
            if isinstance(term, Constant):
                return (), sign * term.value
        
            # 3) Single variable x -> coeff=sign, key=(('x',1),)
            if isinstance(term, Variable):
                return ((term.name, 1),), sign
        
            # 4) A power x^n
            if isinstance(term, Pow) \
               and isinstance(term.base, Variable) \
               and isinstance(term.exponent, Constant):
                return ((term.base.name, term.exponent.value),), sign
        
            # 5) Product of constants, variables, and POWER terms
            if isinstance(term, Mul):
                coeff = sign
                exps  = {}
                for f in term.factors:
                    # unwrap nested Neg in factors too
                    sub_sign = 1
                    while isinstance(f, Neg):
                        sub_sign *= -1
                        f = f.term
                    if isinstance(f, Constant):
                        coeff *= f.value * sub_sign
                    elif isinstance(f, Variable):
                        coeff *= sub_sign
                        exps[f.name] = exps.get(f.name, 0) + 1
                    elif isinstance(f, Pow) \
                         and isinstance(f.base, Variable) \
                         and isinstance(f.exponent, Constant):
                        coeff *= sub_sign
                        exps[f.base.name] = exps.get(f.base.name, 0) + f.exponent.value
                    else:
                        return None, term  # non-polynomial piece
                key = tuple(sorted(exps.items()))
                return key, coeff
        
            # Anything else (Add, Div, etc.)
            return None, term
            
            
        # 2b) bucket everything
        for t in flat:
            key, coeff = monomial_key(t)
            if key is None:
                others.append(t)
            else:
                buckets[key] = buckets.get(key, 0) + coeff
        # 3) Rebuild combined terms
        new_terms = []
        for key, coeff in buckets.items():
            if coeff == 0:
                continue
            term = Constant(coeff)
            for name, power in key:
                term = term * (Variable(name) ** power)
            new_terms.append(term.simplify())

        # 4) Append “others” and finalize
        new_terms.extend(others)
        if not new_terms:
            return Constant(0)
        if len(new_terms) == 1:
            return new_terms[0]
        self.terms = new_terms
        return self
    def substitute(self, var_name, replacement):
        return Add(*(t.substitute(var_name, replacement) for t in self.terms))
    def evaluate(self, env={}):
        return sum(term.evaluate(env) for term in self.terms)
    def __str__(self):
        return " + ".join(map(str, self.terms))

class Mul(Expr):
    def __init__(self, *factors):
        self.factors = list(factors)

    def simplify(self):
        flat_factors = []
        constant = 1
        for factor in self.factors:
            factor = factor.simplify()
            if isinstance(factor, Constant):
                constant *= factor.value
            elif isinstance(factor, Mul):
                flat_factors.extend(factor.factors)
            else:
                flat_factors.append(factor)

        # ── NEW: nothing left except the accumulated constant ──
        if not flat_factors:
            return Constant(constant)

        if constant != 1:
            flat_factors.insert(0, Constant(constant))

        if len(flat_factors) == 1:
            return flat_factors[0]

        self.factors = flat_factors
        return self

    def evaluate(self, env={}):
        result = 1
        for factor in self.factors:
            result *= factor.evaluate(env)
        return result

    def __str__(self):
        def parenthesize(f):
            # Parenthesize if Add, Neg, or Mul with negative constant as first factor
            if isinstance(f, Add) or isinstance(f, Neg):
                return f"({f})"
            if isinstance(f, Mul):
                # check if the first factor is a negative constant
                if isinstance(f.factors[0], Constant) and f.factors[0].value < 0:
                    return f"({f})"
            return str(f)
        return "·".join(parenthesize(f) for f in self.factors)
        
        
    def substitute(self, var_name, replacement):
        return Mul(*(f.substitute(var_name, replacement)
                     for f in self.factors))
                     
class Neg(Expr):
    def __init__(self, term):
        self.term = term

    def simplify(self):
        term = self.term.simplify()
        if isinstance(term, Constant):
            return Constant(-term.value)
        return Neg(term)

    def evaluate(self, env={}):
        return -self.term.evaluate(env)

    def __str__(self):
        return f"¬({self.term})"
        
    def substitute(self, var_name, replacement):
        return Neg(self.term.substitute(var_name, replacement))
        
class Div(Expr):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        n, d = self.numerator.simplify(), self.denominator.simplify()
        if isinstance(n, Constant) and isinstance(d, Constant):
            num = numeric_value(n)
            den = numeric_value(d)
            if den == 0:
                raise ZeroDivisionError("Division by zero!")
            if num % den == 0:
                return Constant(num // den)
            return Div(Constant(num), Constant(den))
        if isinstance(d, Constant) and numeric_value(d) == 1:
            return n
        return Div(n, d)
   
    def substitute(self, var_name, replacement):
        return Div(self.numerator.substitute(var_name, replacement),
                   self.denominator.substitute(var_name, replacement))
                   
    def evaluate(self, env={}):
        return self.numerator.evaluate(env) / self.denominator.evaluate(env)

    def __str__(self):
        num = self.numerator
        den = self.denominator
        if isinstance(num, Constant): n = f"{num}"
        else: n = f"({num})"
        if isinstance(den, Constant): d = f"{den}"
        else: d = f"[{den}]"
        return f"{num}:{den}"

class Root(Expr):
    def __init__(self, radicand, index=2):
        self.radicand = radicand
        self.index = index

    def simplify(self):
        r = self.radicand.simplify()
        n = self.index

        # Rationalize for 1st and 0th roots
        if n == 1:
            return r
        if n == 0:
            raise ValueError("0th root is undefined")
        
        # Root of constant: handle sign and special cases
        if isinstance(r, Constant):
            val = r.value
            if val < 0:
                # Square root of negative: introduce i
                if n % 2 == 0:
                    return Mul(Root(Constant(-val), n), Variable("i")).simplify()
                # Odd roots of negative: real result
                elif n % 2 == 1:
                    return Constant(-((-val) ** (1/n)))
            # Perfect roots only (symbolic otherwise)
            approx = val ** (1/n)
            if isclose(approx, round(approx)):
                return Constant(round(approx))
            # stay symbolic otherwise
        # Root of root: e.g. √(√2) = 2^{1/4}
        if isinstance(r, Root):
            return Root(r.radicand, r.index * n).simplify()
        # x^{m/n} as root
        if isinstance(r, Pow):
            return Pow(r.base, Div(r.exponent, Constant(n))).simplify()
        return Root(r, n)
        
    def evaluate(self, env={}):
        return pow(self.radicand.evaluate(env), 1/self.index)

    def substitute(self, var_name, replacement):
        return Root(self.radicand.substitute(var_name, replacement), self.index)
        
    def __str__(self):
        if isinstance(self.radicand, Constant):
            if self.index == 2:
                return f"√{self.radicand}"
            else:
                return f"[{self.index}√{self.radicand}]"
        else:
            if self.index == 2:
                return f"√({self.radicand})"
            else:
                return f"[{self.index}√({self.radicand})]"

class Equation:
    def __init__(self, left, right):
        self.left = left
        self.right = right


    def isolate(self, var_name: str) -> "Equation":
        """
        Return a new Equation with `Variable(var_name)` alone on the LHS.

        Handles linear additive/multiplicative cases:
            2·y + 3 + x = 7        →   y = (7 − 3 − x) ÷ 2
            −4·x = 20              →   x = 20 ÷ −4
            y + 5 = 0              →   y = −5
        Raises NotImplementedError for non-linear forms (products of variables,
        powers, roots that contain the variable, etc.).
        """
        # ---- helpers -------------------------------------------------
        def contains(e: Expr) -> bool:
            if isinstance(e, Variable):
                return e.name == var_name
            if isinstance(e, Add):
                return any(contains(t) for t in e.terms)
            if isinstance(e, Mul):
                return any(contains(f) for f in e.factors)
            if isinstance(e, (Neg, Div, Root)):
                inner = (
                    e.term if isinstance(e, Neg) else
                    e.numerator if isinstance(e, Div) else
                    e.radicand
                )
                return contains(inner)
            return False

        # ---- 1. Move everything to the left:  left - right = 0 -------
        expr = Add(self.left, Neg(self.right)).simplify()

        # ---- 2. Split additive terms into “var” vs “constant” ---------
        if isinstance(expr, Add):
            var_terms   = []
            const_terms = []
            for t in expr.terms:
                (var_terms if contains(t) else const_terms).append(t)
            if not var_terms:
                raise ValueError(f"{var_name} not found in equation")

            left_side  = Add(*var_terms).simplify()
            right_side = Neg(Add(*const_terms)).simplify()  # change sides
        else:                       # e.g.  2·y  =  6
            if not contains(expr):
                raise ValueError(f"{var_name} not found in equation")
            left_side, right_side = expr, Constant(0)

        # ---- 3. Extract a numerical coefficient from left_side -------
        # Accept   y              → coeff = 1,  core = y
        #          k·y            → coeff = k,  core = y
        if isinstance(left_side, Variable) and left_side.name == var_name:
            coeff, core = Constant(1), left_side

        elif isinstance(left_side, Mul):
            coeff_val  = 1
            other_factors = []
            for f in left_side.factors:
                if isinstance(f, Constant):
                    coeff_val *= f.value
                else:
                    other_factors.append(f)

            # after stripping constants we must be left with *exactly* Variable(var)
            if len(other_factors) != 1 or not isinstance(other_factors[0], Variable) \
               or other_factors[0].name != var_name:
                raise NotImplementedError("non-linear or mixed variable factors")

            coeff, core = Constant(coeff_val), other_factors[0]

        else:
            raise NotImplementedError("isolate() only supports linear terms")

        # ---- 4. Divide to leave the variable alone -------------------
        if coeff.value != 1:
            right_side = Div(right_side, coeff).simplify()

        return Equation(core, right_side.simplify())

    # -----------------------------------------------------------------
    def evaluate(self, env={}):
        return self.left.evaluate(env) == self.right.evaluate(env)

    def __str__(self):
        return f"{self.left} = {self.right}"

    def substitute(self, var_name, replacement):
        """Symbolically replace `var_name` on both sides."""
        return Equation(
            self.left.substitute(var_name, replacement),
            self.right.substitute(var_name, replacement))

def sqrt(val):
    val = as_expr(val)
    return Root(val, 2).simplify()

def root(val, n):
    val = as_expr(val)
    n = as_expr(n)
    return Root(val, n).simplify()

def _expr_pow(self, exponent):
    if isinstance(exponent, (int, float)):
        exponent = Constant(exponent)
    return Pow(self, exponent).simplify()

Expr.__pow__ = _expr_pow

class Pow(Expr):
    def __init__(self, base, exponent):
        self.base     = base
        self.exponent = exponent

    def simplify(self):
        b = self.base.simplify()
        e = self.exponent.simplify()
        if isinstance(b, Constant) and isinstance(e, Constant):
            return Constant(b.value ** e.value)
        if isinstance(e, Constant):
            if e.value == 0: return Constant(1)
            if e.value == 1: return b
        return Pow(b, e)

    def evaluate(self, env={}):
        return self.base.evaluate(env) ** self.exponent.evaluate(env)

    def substitute(self, var_name, repl):
        return Pow(
            self.base.substitute(var_name, repl),
            self.exponent.substitute(var_name, repl)
        )

    def __str__(self):
        # Parenthesize base if it is Add, Sub, Mul, Div, Neg, or Pow
        def need_parens(expr):
            return isinstance(expr, (Add, Mul, Div, Neg, Pow))
        base_str = f"({self.base})" if need_parens(self.base) else str(self.base)
        exp_str  = f"({self.exponent})" if need_parens(self.exponent) else str(self.exponent)
        return f"{base_str}^{exp_str}"
 
def expand(expr):
    """
    Recursively expand:
      * (a + b)·c  → a·c + b·c
      * (a + b)^n  → expanded binomial
      * nested Add/Mul/Pow all the way down
    """
    # 1) Expand sums
    if isinstance(expr, Add):
        # expand each term, then simplify+flatten
        return Add(*(expand(t) for t in expr.terms)).simplify()

    # 2) Expand negation
    if isinstance(expr, Neg):
        inner = expand(expr.term)
        # If it’s a sum, distribute the negation
        if isinstance(inner, Add):
            # -(a+b+...) → -a + -b + ...
            return Add(*(expand(Neg(t)) for t in inner.terms)).simplify()
        # otherwise just negate the expanded term
        return Neg(inner).simplify()

    # 3) Expand products
    if isinstance(expr, Mul):
        # first expand all factors
        facs = [expand(f) for f in expr.factors]

        # if any factor is an Add, distribute over it
        for i, f in enumerate(facs):
            if isinstance(f, Add):
                before, after = facs[:i], facs[i+1:]
                terms = []
                for term in f.terms:
                    # build a new product with one term from the sum
                    new_prod = Mul(*(before + [term] + after))
                    terms.append(expand(new_prod))
                return Add(*terms).simplify()

        # no sums left in factors → just rebuild & simplify
        return Mul(*facs).simplify()

    # 4) Expand powers
    if isinstance(expr, Pow):
        base = expand(expr.base)
        expn = expr.exponent
        # only do binomial‐style expansion for nonnegative integer exponents
        if isinstance(expn, Constant) and isinstance(expn.value, int) and expn.value >= 0:
            if expn.value == 0:
                return Constant(1)
            # repeated multiply+expand
            result = base
            for _ in range(expn.value - 1):
                result = expand(result * base)
            return expand(result)
        # otherwise just expand deeper
        return Pow(base, expand(expn)).simplify()

    # 5) Expand division
    if isinstance(expr, Div):
        return Div(expand(expr.numerator), expand(expr.denominator)).simplify()

    # 6) Leaf: Variable or Constant
    return expr
 
def extract_coeffs(expr, var_name):
    """Return a dict {degree: coefficient} for a polynomial in `var_name`,
    handling Neg(...) and negative constants and monomials."""
    expr = expr.simplify()
    coeffs = {}
    def add(deg, c):
        coeffs[deg] = coeffs.get(deg, 0) + c

    # break into top-level additive terms
    terms = expr.terms if isinstance(expr, Add) else [expr]

    for t in terms:
        t = t.simplify()

        # Flatten Neg to sign, then proceed with factor extraction
        sign = 1
        while isinstance(t, Neg):
            sign *= -1
            t = t.term.simplify()

        # Constants
        if isinstance(t, Constant):
            add(0, sign * t.value)
            continue

        # Mul or monomial
        c = sign
        d = 0
        facs = t.factors if isinstance(t, Mul) else [t]
        for f in facs:
            if isinstance(f, Constant):
                c *= f.value
            elif isinstance(f, Variable) and f.name == var_name:
                d += 1
            elif isinstance(f, Pow) \
                and isinstance(f.base, Variable) and f.base.name == var_name \
                and isinstance(f.exponent, Constant):
                d += f.exponent.value
            else:
                raise ValueError(f"Non-polynomial term: {f}")
        add(d, c)
    return coeffs

def solve_polynomial(expr: Expr, var_name: str) -> list[Expr]:
    """
    Solve a univariate polynomial in var_name.
    - Factor completely.
    - For each factor:
        - Degree 1: solve exactly.
        - Degree 2: solve exactly (quadratic formula, in radicals).
        - Degree ≥3: leave as FormalRoot.
    Returns a list of roots as Expr (including multiplicities).
    """
    from collections import Counter

    # 1) Fully expand and simplify
    p = expand(expr).simplify()
    # 2) Factor
    factored = factor_polynomial(p, var_name)
    # 3) Flatten Mul tree into factors
    if isinstance(factored, Mul):
        factors = factored.factors
    else:
        factors = [factored]

    roots = []
    for f in factors:
        # Each factor should be monic in var_name, i.e. (ax + b), (ax^2 + bx + c), etc.
        # If it's a Constant: ignore (unless it's 0)
        if isinstance(f, Constant):
            continue  
            # only relevant for zero polynomial
        # Extract coefficients
        try:
            coeffs = extract_coeffs(f, var_name)
        except Exception:
            # Non-polynomial, leave as formal root
            roots.append(FormalRoot(f, varname=var_name))
            continue

        deg = max(coeffs)
        arr = [coeffs.get(d, 0) for d in range(deg, -1, -1)]
        arr = [Constant(x) for x in arr]     
        # Degree 1: ax + b = 0
        if deg == 1:
            a, b = arr
            a = algebraic(a)
            b = algebraic(b)
            root = Div(Constant(-b), Constant(a)).simplify()
            roots.append(root)
        # Degree 2: ax^2 + bx + c = 0
        elif deg == 2:
            a, b, c = arr
            a = algebraic(a)
            b = algebraic(b)
            c = algebraic(c)
            # Quadratic formula: (-b ± √(b²-4ac)) / (2a)
            discriminant = Add(Mul(Constant(b), Constant(b)), Neg(Mul(Constant(4), a, c))).simplify()
            sqrt_disc = Root(discriminant, 2).simplify()
            denom = Mul(Constant(2), a).simplify()
            roots.append(Div(Add(Neg(Constant(b)), sqrt_disc), denom).simplify())
            roots.append(Div(Add(Neg(Constant(b)), Neg(sqrt_disc)), denom).simplify())
        # Degree ≥ 3: formal root
        else:
            # For each root (multiplicity), use FormalRoot
            multiplicity = coeffs.get(0, 1)  # Not always accurate, but...
            # If the polynomial is reducible, degree will be 1 per linear, 2 per quad, ≥3 per factor
            for i in range(deg):
                roots.append(FormalRoot(f, which=i+1, varname=var_name))
    return roots

def divisors(n):
    """Return all integer divisors (±) of n."""
    n = int(n)
    res = set()
    for i in range(1, abs(n)+1):
        if n % i == 0:
            res.add(i); res.add(-i)
    return res

def synthetic_division(coefs, root):
    """
    Synthetic divide list [a_n,...,a_0] by (x - root).
    Returns (quotient_list, remainder).
    """
    out = []
    acc = 0
    for a in coefs:
        acc = a + acc*root
        out.append(acc)
    return out[:-1], out[-1]


# ────────────────────────────────────────────────────────────
# 3) Factorization routine
# ────────────────────────────────────────────────────────────
def factor_polynomial(expr, var_name):
    """
    Factor a univariate polynomial with integer coeffs by peeling off
    integer roots one at a time (synthetic division).
    Returns an Expr that is the product of linear factors and the leftover polynomial.
    """
    # 1) pull out coefficients
    coeffs = extract_coeffs(expr, var_name)
    deg = max(coeffs)
    arr = [coeffs.get(d, 0) for d in range(deg, -1, -1)]

    # 2) peel off linear factors (x - r) for integer roots r
    factors = []
    while len(arr) > 1:
        found = False
        for r in divisors(arr[-1]):
            q, rem = synthetic_division(arr, r)
            if rem == 0:
                factors.append(Add(Variable(var_name), Constant(-r)))
                arr = q
                found = True
                break
        if not found:
            break

    # 3) rebuild any leftover polynomial
    if len(arr) > 1:
        terms = []
        highest = len(arr) - 1
        for i, c in enumerate(arr):
            p = highest - i
            mon = (Variable(var_name) ** p) if p else Constant(1)
            terms.append(Constant(c) * mon)
        remainder = Add(*terms).simplify()
    else:
        remainder = Constant(arr[0])

    # 4) assemble final product
    result = None
    for F in factors:
        result = F if result is None else Mul(result, F)
    if remainder is not None:
        result = remainder if result is None else Mul(result, remainder)

    return result.simplify()
 
class Matrix:
    def __init__(self, rows):
        # rows: iterable of iterables of Expr or scalars
        self.data = [
            [algebraic(e) for e in row]
            for row in rows
        ]
        self.n, self.m = len(self.data), len(self.data[0])
        if any(len(r) != self.m for r in self.data):
            raise ValueError("All rows must have the same length")

    def __str__(self):
        # simple row-by-row display
        row_strs = []
        for row in self.data:
            row_strs.append("[ " + ", ".join(str(e) for e in row) + " ]")
        return "[\n  " + "\n  ".join(row_strs) + "\n]"

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Can only add Matrix to Matrix")
        if (self.n, self.m) != (other.n, other.m):
            raise ValueError("Matrix dimensions must agree")
        return Matrix([
            [ self.data[i][j] + other.data[i][j]
              for j in range(self.m) ]
            for i in range(self.n)
        ])

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.m != other.n:
                raise ValueError("Inner dimensions must agree")

            return Matrix([
                [
                  # start from Constant(0), then sum and simplify
                  sum(
                    (self.data[i][k] * other.data[k][j]
                     for k in range(self.m)),
                    Constant(0)
                  ).simplify()
                  for j in range(other.m)
                ]
                for i in range(self.n)
            ])

        else:
            # scalar multiplication unchanged
            return Matrix([
                [ algebraic(other) * e for e in row ]
                for row in self.data
            ])

    def __rmul__(self, other):
        return self * other

    def evaluate(self, env={}):
        """Return a new Matrix whose entries are Constant(evaluate(env))."""
        evaluated = [
            [ Constant(e.evaluate(env)) for e in row ]
            for row in self.data
        ]
        return Matrix(evaluated)

    def substitute(self, var_name, replacement):
        """Symbolic substitution in each entry."""
        return Matrix([
            [ e.substitute(var_name, replacement) for e in row ]
            for row in self.data
        ])

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Can only subtract Matrix from Matrix")
        if (self.n, self.m) != (other.n, other.m):
            raise ValueError("Matrix dimensions must agree")
        return Matrix([
            [
                self.data[i][j] - other.data[i][j]
                for j in range(self.m)
            ]
            for i in range(self.n)
        ])

    @staticmethod
    def identity(n):
        """Return the n×n identity matrix."""
        return Matrix([
            [Constant(1) if i == j else Constant(0) for j in range(n)]
            for i in range(n)
        ])

    def determinant(self):
        """Compute det(self) by Laplace expansion."""
        if self.n != self.m:
            raise ValueError("Determinant only defined for square matrices")
        # 1×1 base case
        if self.n == 1:
            return self.data[0][0]
        # 2×2 fast path
        if self.n == 2:
            a, b = self.data[0]
            c, d = self.data[1]
            return (a * d - b * c).simplify()

        # general n×n
        det = Constant(0)
        for j in range(self.m):
            elem = self.data[0][j]
            # build minor by removing row 0 and column j
            minor_rows = [
                [ self.data[i][k]
                  for k in range(self.m) if k != j ]
                for i in range(1, self.n)
            ]
            cofactor = elem if (j % 2 == 0) else Neg(elem)
            det = det + cofactor * Matrix(minor_rows).determinant()
        return det.simplify()

    def charpoly(self, var_name="λ"):
        """Return the characteristic polynomial det(M – λI)."""
        lam = Variable(var_name)
        lamI = Matrix.identity(self.n) * lam  
        return (self - lamI).determinant().simplify()

    def eigenvalues(self, var_name="λ"):
        """
        Factor the characteristic polynomial and extract the linear roots.
        Returns a list of Constant roots (with multiplicity).
        """
        """Return *all* roots (including unsolved formal ones)."""
        charpoly = self.charpoly(var_name)
        return solve_polynomial(charpoly, var_name)
        #    def eigenvalues(self, var_name="λ"):
        #cp = expand(self.charpoly(var_name)).simplify()
        #return solve_polynomial(cp, var_name)
        # 1) build and expand the char. poly
        p = expand(self.charpoly(var_name)).simplify()
        # 2) factor it
        f = factor_polynomial(p, var_name)

        # 3) collect all linear factors of form (λ + c) → root = -c
        roots = []
        factors = [f] if isinstance(f, Add) else (f.factors if isinstance(f, Mul) else [])
        for fac in factors:
            if isinstance(fac, Add):
                c = 0
                for term in fac.terms:
                    if isinstance(term, Constant):
                        c = term.value
                roots.append(Constant(-c))
        return roots
        
    def algebraic_multiplicities(self, var_name="λ"):
        """
        Return a dict {eigenvalue: multiplicity}, where eigenvalue is a Constant.
        """
        evs = self.eigenvalues(var_name)
        mults = {}
        for root in evs:
            mults[root] = mults.get(root, 0) + 1
        return mults

class FormalRoot(Expr):
    def __init__(self, poly, which=1, varname="x"):
        self.poly = poly # the polynomial as Expr
        self.which = which # which root (if multiple)
        self.varname = varname
    def __str__(self):
        # Root number only for display
        p = expand(self.poly).simplify()
        suffix = f"_{self.which}"
        return f"｛{self.varname}{suffix}:| ({p} = 0)｝"
    def __repr__(self):
        return str(self)
    
########## TEST ###########
x = Var("x")
# Given your original algebra classes (Expr, Variable, Constant, Add, Mul, etc.)

expr = 2*x + 5    # 2*x + 5
expr2 = x + 2     # x + 2
expr3 = 4 - x     # 4 - x (correctly handled via __rsub__)
expr4 = x - 4     # x - 4
expr5 = 2 * (x**2 - 1)    # 2*(x^2 - 1)
expr6 = (x + 1) * 3       # (x + 1)*3
print(expr)
print(expr2)
print(expr3)
print(expr4)
print(expr5)
print(expr6)

print(Div(Constant(2), Constant(3)))
print(Root(Constant(2)))
print(Root(Add(Constant(2), Root(Constant(3)))))
print(Add(Constant(2), Root(Constant(3))))
print(Add(Constant(1), Mul(Constant(1), Variable("i"))))
print(pi)
print(euler)
print(im)

# Usage example
x = Constant(2) * Root(Constant(2))
y = Constant(3) + Constant(-3) + Variable("x") + Variable("y") + Constant(4)
eq = Equation(y, Constant(10))

print("x =", x)
print("y =", y)
print("Equation:", eq)
print("Isolated x:", eq.isolate("x"))
print("Evaluate equation (x=2, y=4):", eq.evaluate({"x": 2, "y": 4}))


x = Var("x")
# Define equation: 2·x + 3 = 7
equation = Equation(Constant(2) * x + Constant(3), Constant(7))

# Isolate x
isolated_eq = equation.isolate("x")
print("Isolated Equation:", isolated_eq)

# Evaluate isolated equation for validation
print("Evaluate for x=2:", isolated_eq.evaluate({"x": 2}))

x, y = Variable("x"), Variable("y")
eq_xy = Equation(x, y)      # x = y
print(eq_xy)                # →  x = y

# symbols
x, y = Variable("x"), Variable("y")
a, b = Var("x"), Var("y")

# an expression
expr = Mul(Constant(2), x) + Constant(3)     # 2·x + 3
print(expr)                                  # → 2·x + 3

# substitute x → y
expr_xy = expr.substitute("x", Mul(Constant(2), y))
print(expr_xy)                               # → 2·y + 3


# an equation
eq = Equation(expr_xy, Constant(7))          # 2·x + 3 = 7
print(eq)                                    # → 2·x + 3 = 7

# same equation, but with x replaced by y
eq_xy = eq.substitute("x", Constant(2))      # 2·y + 3 = 7
print(eq_xy)                                 # → 2·y + 3 = 7

# isolate y
iso = eq_xy.isolate("y")
print(iso)                                   # → y = (7 + -3)÷2  →   y = 2
x, y = Variable("x"), Variable("y")

# 1) 2·y + 3 + x = 7      →     y = (7 − 3 − x) ÷ 2
eq1 = Equation(Add(Mul(Constant(2), y), Constant(3), x), Constant(7))
print(eq1.isolate("y"))
# ⇒ y = (7 + -3 + -x)÷2

# 2) -4·x = 20            →     x = 20 ÷ -4
eq2 = Equation(Mul(Constant(-4), x), Constant(20))
print(eq2.isolate("x"))
# ⇒ x = (20)÷(-4)

# 3) y + 5 = 0            →     y = -5
eq3 = Equation(Add(y, Constant(5)), Constant(0))
print(eq3.isolate("y"))
# ⇒ y = -5

print("*"*5)
x = Variable("x")
# P(x) = x³ − 3·x² + 2·x
P = x*x*x - Constant(3)*(x*x) + Constant(2)*x

x = Variable("x")
poly = Add(
    Pow(x, Constant(3)),
    Mul(Constant(-6), Pow(x, Constant(2))),
    Mul(Constant(11), x),
    Constant(-6)
)
print("Polynomial:", poly)
print("Factored :", factor_polynomial(poly, "x"))


x = Variable("x")
poly = x**3 + Constant(-6)*x**2 + Constant(-1)*x + Constant(6)

print("Polynomial:", poly)
print("Factored :", factor_polynomial(poly, "x"))

poly = x**2 + -2*x + 1
print("Polynomial:", poly)
print("Factored :", factor_polynomial(poly, "x"))

x = Variable("x")
poly = x**3 - 6*x**2 + 11*x - 6
print("Polynomial:", poly)
print("Factored :", factor_polynomial(poly, "x"))

x = Var("x")
poly = (x - 1)**2
print("Polynomial before expand:", poly)
expanded = expand(poly)
print("Expanded:", expanded)
print("Factored:", factor_polynomial(expanded, "x"))

x = Var("x")
poly  = (x - 1)**5
print("Expand :", expand(poly))
print("Factored:", factor_polynomial(expand(poly), "x"))

x = Var("x")
poly  = (x - 1)**5 + 1
print("Expand :", expand(poly))
print("Factored:", factor_polynomial(expand(poly), "x"))

# 1) Build two 2×2 symbolic matrices
x, y = Var("x"), Var("y")
A = Matrix([[1, x],
            [y, 2]])
B = Matrix([[x, 3],
            [4, y]])

print("A =", A)
print("B =", B)

# 2) Add
C = A + B
print("A + B =", C)

# 3) Scalar multiply
D = 2 * A
print("2·A =", D)

# 4) Matrix multiply
E = A * B
print("A·B =", E)

# 5) Substitute x→5, y→7
F = E.substitute("x", Constant(5)).substitute("y", Constant(7))
print("After x=5,y=7:", F)

G = F.evaluate()
print("After x=5,y=7:", G)

# Build a simple 2×2 matrix
x = Var("x")
A = Matrix([[2, 1],
            [1, 2]])

print("A =")
print(A)

# 1) determinant
print("det(A) =", A.determinant())
# → det = 3

# 2) characteristic polynomial
cp = A.charpoly("λ")
print("charpoly(λ) =", cp)
# → x^2 + -4·x + 3

# 3) eigenvalues
evs = A.eigenvalues("x")
print("eigenvalues:")
for ev in evs:
    print("  - λ:", ev)
# → [ Constant(1), Constant(3) ]

A = Matrix([[3,1],[2,2]])
cp = A.charpoly("λ")    # → charpoly(l) = -1 + (2 + -(l))·(2 + -(l))
print("Characteristic Polynomial")
print("Det(A-λI) =", cp)
print("  =", expand(cp).simplify())

print("\nEigenvalues:")
for ev in A.eigenvalues("λ"):
    print("  -", ev)

print("\nAlgebraic multiplicities:")
mults = A.algebraic_multiplicities("λ")
for ev, mult in mults.items():
    print(f"  λ = {ev!s:<3}  Alg. multiplicity = {mult}")
    
A = Matrix([
    [5, 1, 1],
    [0, 2, 1],
    [1, 1, 1]])
print("A=")
print(A)

cp = A.charpoly("λ")    # → charpoly(l) = -1 + (2 + -(l))·(2 + -(l))
print("Characteristic Polynomial")
print("Det(A-λI) =", cp)
print("  =", expand(cp).simplify())

print("\nEigenvalues:")
for ev in A.eigenvalues("λ"):
    print("  -", ev)

print("\nAlgebraic multiplicities:")
mults = A.algebraic_multiplicities("λ")
for eigenval, multiplicity in mults.items():
    print(f"Eigenvalue λ = {eigenval}, algebraic multiplicity = {multiplicity}")

A = Matrix([
#    [Var("t"),1, 1],
    [2,1, 1],
    [0,2, 1],
    [1,1, 1]])
print("A=")
print(A)

cp = A.charpoly("λ")    # → charpoly(l) = -1 + (2 + -(l))·(2 + -(l))
print("Characteristic Polynomial")
print("Det(A-λI) =", cp)
print("  =", expand(cp).simplify())

A5 = A.substitute("t", Constant(5))
print(A5)
evs = A5.eigenvalues("λ")
for ev in evs:
    print("  - λ:", ev)

evs = A.eigenvalues("λ")
for ev in evs:
    print("  - λ:", ev)

mults = A.algebraic_multiplicities("λ")
for eigenval, multiplicity in mults.items():
    print(f"Eigenvalue λ = {eigenval}, algebraic multiplicity = {multiplicity}")
print("="*7)
x = Var("x")
print("√2 stays as symbolic:", Root(Constant(2)).simplify())
print("2÷3 stays as symbolic:", Div(Constant(2), Constant(3)).simplify())
print("√-2 becomes i√2:", Root(Constant(-2)).simplify())
print("√(x^2+1) stays formal:", Root(Add(Pow(x, Constant(2)), Constant(1))).simplify())
print("√(√2):", Root(Root(Constant(2))).simplify())
print("π is transcendental:", Variable("π"))
print("2 + √3:", Add(Constant(2), Root(Constant(3))).simplify())


# Formal unsolved root (eigenvalue of x^3 + x + 1 = 0)
poly = Add(Pow(x, Constant(3)), x, Constant(1))
formal_root = FormalRoot(poly)
print("Unsolved cubic eigenvalue:", formal_root)
# → [1, 3]

x = Var("x")
# Example 1: x^3 + x + 1 (irreducible cubic)
poly1 = Add(Pow(x,Constant(3)), x, Constant(1))
print("Roots for x^3 + x + 1 = 0:", solve_polynomial(poly1, "x"))
# Output: [Root(x^3 + x + 1 = 0, x)]

# Example 2: x^4 - 1 (factorable)
poly2 = Add(Pow(x,Constant(4)), Neg(Constant(1)))
print("Roots for x^4 - 1 = 0:", solve_polynomial(poly2, "x"))
# Output: [1, -1, Root(x^2 + 1 = 0, x)] (i.e., 1, -1, i, -i)

# Example 3: x^2 - 2
poly3 = Add(Pow(x,Constant(2)), Neg(Constant(2)))
print("Roots for x^2 - 2 = 0:", solve_polynomial(poly3, "x"))
# Output: [√2, -√2]

# x^2 - 3x + 2 = (x-1)(x-2)
x = Var("x")
poly = x**2 + -3*x + 2
print("Roots:", solve_polynomial(poly, "x"))
# Expect: [2, 1]

# x^2 - 2 = 0
poly = x**2 + -2
print("Roots:", solve_polynomial(poly, "x"))
# Expect: [√2, -√2]
# x^2 + 1 = 0
poly = x**2 + 1
print("Roots:", solve_polynomial(poly, "x"))
# Expect: [i, -i]
# x^3 + x + 1 = 0
poly = x**3 + x + 1
print("Roots:", solve_polynomial(poly, "x"))
# Expect: [FormalRoot(x^3 + x + 1)]
# x^4 - 1 = (x^2 - 1)(x^2 + 1) = (x-1)(x+1)(x^2 + 1)
poly = x**4 - 1
print("Roots:", solve_polynomial(poly, "x"))
# Expect: [1, -1, i, -i]
A = Matrix([
    [0, 0, -1],
    [1, 0, -1],
    [0, 1, -1]
])

cp = A.charpoly("λ")
print("Characteristic Polynomial:", cp)
roots = solve_polynomial(cp, "λ")
print("Eigenvalues:", roots)
# Expect: [FormalRoot(...)]

A = Matrix([
    [2, -1, 0],
    [0, 2, -1],
    [0, 0, 2]
])
cp = A.charpoly("λ")
print("Characteristic Polynomial:", cp)
roots = solve_polynomial(cp, "λ")
print("Eigenvalues:", roots)
# Expect: [2, 2, 2]

A = Matrix([[0, 0, -1], [1, 0, -1], [0, 1, -1]])
cp = A.charpoly("λ")
lambdas = solve_polynomial(cp, "λ")
print("Eigenvalues (lambdas):")
for lam in lambdas:
    print("  λ =", lam)
# The only thing you can do is return the FormalRoot object:
lam = FormalRoot(cp, varname="λ")
print("λ:", lam)


# x^3 + x + 1 = 0 has 3 formal roots
x = Var("x")
poly = x**3 + x + 1
roots = solve_polynomial(poly, "x")
print("Roots:", roots)
print("Algebraic multiplicity:", len(roots))

# x^3 + x + 1 = 0 has 3 formal roots
x = Var("x")
poly = x**3 + x + 1
roots = solve_polynomial(poly, "x")
print("Roots:", roots)
print("Algebraic multiplicity:", len(roots))

