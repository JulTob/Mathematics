> $Sets$ are to categorizations what numbers are to counting.

# 🌌 **The Universe of Sets**

In the grand narrative of mathematics, set theory stands as the foundation upon which the vast cosmos of mathematical ideas is built. Like stars forming constellations, every number, shape, and mathematical resides in a **set**. 

At its core, **set theory** is the study of **collections of objects**, known as **elements**. These objects might be numbers, letters, geometric shapes, or even other sets. 

> <h4 style="color:DodgerBlue;">Set:</h1>
> A well-defined collection of distinct objects, known as elements.

Like galaxies in the universe, sets bring unity to diverse elements, but they do so without any particular order. The absence of order allows us to focus on the relationship between elements and their membership within sets.











### 🌠 **Symbols of Set Theory**:
The elegant language of set theory uses symbols to express the relationships between sets and their elements. 

- **$\color{goldenrod}\in$, $\color{goldenrod}\notin$**: Indicates whether an element is in or not in a set.

$$
\color{goldenrod}
𝟸 ∈ ℕ
$$

- **$\color{violet}\emptyset$**: Represents the **empty set**, a set containing no elements.
$$
\color{violet}
\emptyset = \{\}
$$

- **$\color{gold}\subset$, $\color{gold}\supset$**: Represent **subsets** and **supersets**, hierarchical structures within the universe of sets.
$$
\color{goldenrod}
｛1, 2｝ \subseteq ｛1, 2, 3｝
$$

- **$\color{aqua}\cup$, $\color{aqua}\cap$**: Represents intersection (common elements) and union (combined elements) of sets.
$$
\color{aqua}
A \cap B = {x : x \in A \text{ and } x \in B}
$$

$$
\color{aqua}
A \cup B = ｛x : x \in A \text{ or } x \in B｝
$$

- $\color{tomato}\setminus$ : Denotes set difference, removing elements of one set from another.
$$
\color{tomato}
A \setminus B = ｛x \in A : x \notin B｝
$$

- **$\color{gold}\complement$**: The **complement** of a set, representing everything **outside** a given set.

$$
\color{gold}
\begin{array}{lll}
    \color{goldenrod}{𝑎∈𝑨}     &:& \text{𝑎 Is an element of 𝑨}   \\
    \textcolor{tomato}{𝑎∉𝑨}     &:& \text{𝑎 Is not an element of 𝑨}   \\
    \\
    \textcolor{red}{∅}     &:& \text{The empty set} \\ 
    \\
    𝑨 ⊂ 𝑩     &:& \text{𝑨 Is a subset of 𝑩} \\
    𝑨 ⊃ 𝑩    &:& \text{𝑨 Is a superset of 𝑩} \\
    𝑨 ⊆ 𝑩     &:& \text{𝑨 Is a subset, possibly equal 𝑩} 
    \\
    𝑨 ⊇ 𝑩    &:& \text{Is a superset, possibly equal} \\ 
    \\
    A = B &:& \text{Sets A and B are equal}   \\
    A ≠ B &:& \text{Sets A and B are not equal}   \\
    A ⋂ B &:& \text{Intersection of sets A and B (Elements common to both)}   \\
    A ⋃ B &:& \text{Union of sets A and B (Elements in either or both)}   \\
    \\
    A^c   &:& \text{The complement of set A (Everything outside of A)}   \\
    \end{array}
$$

$$
\color{gold}
\begin{matrix}
    \color{goldenrod}{𝑎∈𝑨}     &:& \text{𝑎 Is an element of 𝑨}   \\
    \textcolor{tomato}{𝑎∉𝑨}     &:& \text{𝑎 Is not an element of 𝑨}   \\
    \textcolor{red}{∅}     &:& \text{The empty set} \\ 
    𝑨 ⊂ 𝑩     &:& \text{𝑨 Is a subset of 𝑩} \\
    𝑨 ⊃ 𝑩    &:& \text{𝑨 Is a superset of 𝑩} \\
    𝑨 ⊆ 𝑩     &:& \text{𝑨 Is a subset, possibly equal 𝑩} 
    𝑨 ⊇ 𝑩    &:& \text{Is a superset, possibly equal} \\ 
    A = B &:& \text{Sets A and B are equal}   \\
    A ≠ B &:& \text{Sets A and B are not equal}   \\
    A ⋂ B &:& \text{Intersection of sets A and B (Elements common to both)}   \\
    A ⋃ B &:& \text{Union of sets A and B (Elements in either or both)}   \\
    A^c   &:& \text{The complement of set A (Everything outside of A)}   \\
    \end{matrix}
$$

These tools allow us to express relationships with precision, like celestial maps charting the universe.

---






## 🌠 What Makes a Set?

🔭 A set is **well-defined** if any object can decisively be identified as either a member of the set or not. This clarity is essential for mathematical rigor.

📋 Example: The set of even numbers is well-defined:
$$
\color{Lime}
2 ∈ \text{Even}
$$

$$
\color{Tomato}
3 ∉ \text{Even}
$$

There are two main ways to define a set:
1. ### Explicit Listing
   Sets can be constructed by directly listing their elements
$$
\color{silver}
\text{Planets in the Solar System} = \{\text{Mercury}, \text{Venus}, \text{Earth}, \text{Mars}, \text{Jupiter}, \text{Saturn}, \text{Uranus}, \text{Neptune}\}
$$

1. ### Property-based Definition
   We can also define sets by describing a **Property** that its elements must satisfy.
   A Property $(𝑃(𝑎))$ is a statement about $𝑎$ with Boolean (`True/False`) value.
$$
\color{#F42C04}
𝔸 = \{ 𝑎 : 𝑃(𝑎) \}
$$
Where 𝑃(𝑎) represents a condition that defines membership in the set.

📋 In this example, the set includes all real numbers between $-1$ and $1$, inclusive:
$$
0 ∈ \{ r : r \in \mathbb{R}, |r| \leq 1 \}
$$
📋 Another example, the set of **even numbers** can be defined as:
$$
\color{#FF70A6}
\text{Even} = \{ a : a \mod 2 = 0 \}
$$










---

## 🌌 **Subsets and Proper Subsets**

In the hierarchy of sets, a subset $A$ is contained within another set $B$ if every element of $A$ is also an element of $B$:

$$
\color{#0093F5}
𝔸 ⊆ 𝔹 \text{ if   } (∀𝑥)(𝑥∈𝔸 ⟹ 𝑥∈𝔹 )
$$


A proper subset contains fewer elements than its superset:

$$
\color{#0093F7}
𝔸 ⊂ 𝔹 \text{ if   } (∀𝑥)(𝑥∈𝔸 ⟹ 𝑥∈𝔹 )
$$

📋 Example:
$$
\color{#0093F6}
\text{Mammals }  ⊂   \text{ Animals}
$$





---

## 🪐 **Universal Set and Complements**

The universal set $U$ contains all objects under consideration in a given context. 

The **complement** of a set $𝔸$, denoted **$𝔸^∁$**, represents all elements in the universal set that are **not in $𝔸$**.

---

## 🌌 **Cardinality: Measuring the Size of Sets**

The cardinality of a set is its size:

- **Finite sets**: $|S|$ is simply the number of elements in $S$.
  $|{1, 2, 3}| = 3$
- **Infinite sets**: These have cardinalities that cannot be expressed with a finite number. For example, the set of natural numbers **$ℕ$** is infinite, yet it has the same cardinality as the set of even numbers.

Example:
$$
|∅| = 0
$$

---

## 🚀 **Finite and Infinite Sets**

In the boundless realm of sets, we encounter two great categories: finite and infinite.

* ### 🌟 Finite Sets
  A finite set contains a specific, countable number of elements. Its size, or cardinality, is a natural number:

$$
    |A| = n \quad \text{where} \quad n \in \mathbb{N}
$$

* ### 🌟 **Infinite Sets**
  An infinite set defies finite bounds, stretching endlessly into the mathematical cosmos. Infinite sets are uncountable or infinitely countable.
  - The natural numbers form an infinite set: 
  $$
  ℕ = \{1, 2, 3, 4, \dots\}
  $$
  - The real numbers between $0$ and $1$ also form an infinite set, but their cardinality is much greater, as they are uncountable.
---

# ⭐ **Comparing Sets**

Two sets are **equal** if they contain exactly the same elements, regardless of order or repetition:
$$
\left\{a, b, c \right\} = \left\{c, b, a \right\}
$$

---

## 🌌 **Types of Sets: Finite and Infinite Explorations**

Finite sets are akin to tiny islands, their elements easily countable. Infinite sets, by contrast, resemble vast oceans, their elements stretching beyond imagination.

📋 One famous example of an infinite set is the Fibonacci sequence, defined by a recurrence relation:

$$
\text{Fibonaccis} := \{ x(i) : x(i) = x(i-1) + x(i-2), \, i \geq 2 \, \text{with} \, x(0) = 1, \, x(1) = 1 \}
$$
This sequence starts as:  $\{1,1,2,3,5,8,13,…\}$

Here, each element emerges as the sum of the two preceding ones, embodying the harmony of infinite patterns within the finite.
---

### **The Set as a Foundation**

In the **universe of mathematics**, sets are the fundamental building blocks from which everything else is constructed. Whether finite or infinite, explicit or implicit, sets help us **navigate** the vast space of mathematical ideas, offering a powerful framework for **understanding** and **organizing** the world.

Each set is a **constellation**, a pattern in the night sky, guiding us toward deeper understanding as we explore the endless universe of mathematics. It invites us to discover patterns, ask questions, and seek connections, just as the night sky inspires wonder. Sets remind us that within every collection lies a story waiting to be understood.



***
# Test yourself:
- 🧩 Is `2` in the set `{1,{2}}`?
> No. {2} ∈ {1,{2}} but 2∉ {1,{2}}.

- 🧩 Is the statement true? `{1,3,5} = {3,5,1}= {1,5,1,3}`
  > Yes. Order or repetition don't matter in sets.

- 🧩 Is this statement true? 
{ $x$ | $x∈ℝ$ , $x^2$ − $2x$ + 1 = 0} = {1},
> Yes. As $x^2$ − $2x$ + 1 = $(x-1)^2$

- 🧩 Is this statement true? 
{ $x$ | $x∈ℝ$ , $x^2$ + 1 = 0} = the set of female popes
> Yes. Both are equal to $∅$

- 🧩 What are the subsets of {1,2}
> {1,2}, {1}, {2}, ∅


$$

# Define two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Common set operations

print("Union:", A | B)          # {1, 2, 3, 4, 5, 6}
print("Intersection:", A & B)   # {3, 4}
print("Difference (A - B):", A - B)  # {1, 2}
$$

$$
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference (A - B): {1, 2}
$$

