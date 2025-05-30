# **Relations: Applications and Functions**

# 🌌 Relations and Equivalence in Mathematics 🌌

Relations describe connections or interactions between elements of sets. 

While sets represent collections of objects, relations describe how these objects interact or connect.


A relation is a mathematical tool that links elements, creating a framework where elements interact according to specific rules.


---

# 🔷 Relations Between Sets $(𝓡)$

🏵 A **relation** $𝓡$ between the elements of sets $𝔸$ and $𝔹$, is a subset of the **Cartesian product** of the sets. 

```math
\color{lime}
𝓡⊆𝔸×𝔹
```

In simpler terms, it describes pairs of elements within the sets that are related in some way:


- if $(𝕒,𝕓) ∈ 𝓡$, we say that
  - $𝓡$ is satisfied by $(𝕒,𝕓)$
  - $𝕒$ is related to $𝕓$ by $𝓡$

- When $𝔸$ and $𝔹$ are the same set, $𝓡⊆𝔸×𝔸$, and we call $𝓡$ a relation on $𝔸$.

> [!NOTE]
> Notation: $a𝓡b$ means $(a,b) ∈ 𝓡$.



> ## 📒 Relations

> *_Subset Relation:_*
> ```math
> 𝓡 =｛(U,V) ∈ 𝒫(A)×𝒫(A) ∣ U⊆V｝
> ```
> Describes the subset relation between subsets of $A$.

> **Membership Relation:**
> ```math
> 𝓡 = \{ (a,S) ∈ A×𝒫(A) ∣ a∈S \}
> ```
> Relates elements $a$ to subsets $S$ where $a∈S$.





# 🔷 Important Classes of Relations

### Functions
Functions are a specific type of relation where each element in $𝔸$ is related to exactly one element in $𝔹$.

### Equivalences
Equivalence relations group elements into classes, where members share a defined relationship.
> Relationship: "Has the same color." The equivalence classes are groups of mugs, where each group contains only mugs of a single color. 
> - 🟥 The "red" equivalence class contains all red mugs.
> - 🟦 The "blue" equivalence class contains all blue mugs.
---








# ⚜️ Properties of Relations

A relation $𝓡$ on a set $A$ can have the following properties:

- 🔵 Reflexive
  * $(a,a)∈R$ for all $a∈A$ 
  * Every element relates to itself.

- 🟢 Symmetric
  * If $(a,b)∈R$, then $(b,a)∈R$ 
  * Relation holds both ways.

- 🟡 Antisymmetric
  * If $(a,b)∈R$ and $(b,a)∈R$, then $a=b$.
  * The relation holds in one direction unless the elements are identical.

- 🟠 Transitive
  * If $(a,b)∈R$ and $(b,c)∈R$, then $(a,c)∈R$.
  * The relation extends through intermediary elements.


---











### 🧊 **Reflexive**

A relation $𝓡$ is **reflexive** if every element in the set is related to itself:

```math
(𝓊, 𝓊) ∈ 𝓡 
```
```math
𝓊𝓡𝓊 \text{  for all } 𝓊∈U
```
```math
𝓊~𝓊 
```
Graphically, this corresponds to the diagonal in the Cartesian plane where $𝓍=𝓎$.

> **Example:** In the set of real numbers $ℝ$, the relation $≤$ is reflexive because every number is less than or equal to itself:

> ```math
> x≤x \, \text{for all}\, x∈ℝ
> ```








### ⭐️ **Symmetric**
A relation $𝓡$ is **symmetric** if, for any two elements $𝓊$ and $𝓋$:


```math
𝓊 𝓡 𝓋  ⟹ 𝓋 𝓡 𝓊
```
- If $𝓊$ is related to $𝓋$, then $𝓋$ is also related to $𝓊$.

> In the set of people, the relation "is a sibling of" is symmetric because if Alice is a sibling of Bob, then Bob is a sibling of Alice.

### 🔥 **Antisymmetric**

A relation $𝓡$ is **antisymmetric** if, for any two elements $𝓊$ and $𝓋$:

```math
𝓊 𝓡 𝓋 ∧ 𝓋 𝓡 𝓊 ⟶ 𝓊 = 𝓋 
```
> The $≤$ relation on real numbers is antisymmetric:  
> If $𝑥 ≤ 𝑦$ and $𝑦 ≤ 𝑥$, then $𝑥 = 𝑦$.


---
### 🛹 Transitive

A relation $𝓡$ is **transitive** if, whenever $𝓊$ is related to $𝓋$ and $𝓋$ to $𝓌$:

```math
𝓊 𝓡 𝓋 ∧ 𝓋 𝓡 𝓌 ⟹ 𝓊 𝓡 𝓌 
```

> In a family tree, if Alice is an ancestor of Bob and Bob is the ancestor of Charlie, then Alice is the ancestor of Charlie.







---

# 🌌 **Equivalence Relations**

🏵 $𝓔$ is an equivalence relation on $A$ if it satisfies:
1. Reflexivity: 
  - $(a,a)∈𝓔$ .
  - $\color{tomato} a∼a$
2. Symmetry
  > - If $(a,b)∈𝓔$, then $(b,a)∈𝓔$.
  > > $\color{tomato}a∼b ⟶ b∼a$
3. #### Transitivity
  > - If $(a,b)∈𝓔$ and $(b,c)∈𝓔$, then $(a,c)∈𝓔$.
  > > $\color{tomato}(a∼b ⋀ b∼c) ⟶ a∼c$

> > $(a,b)∈𝓔$ $\color{tomato}:= (a∼b)$

> [!IMPORTANT]
> ```math
> \text{For a relation } 𝓔 \text{ in } 𝕌: 
> 𝓔 \text{ is an equivalence relation if it satisfies reflexivity, symmetry, and transitivity.}
> ```
> 𝒬 on 𝕌 is equivalent if
> Reflexive    𝓊𝓔𝓊
> Symmetric    𝓊𝓔𝓋⟶𝓋𝓔𝓊
> Transitive   𝓊𝓔𝓋⋀𝓋𝓔𝓌⟶𝓊𝓔𝓌
> ```
> ```
---






## ⚜️ Equivalence Classes
An equivalence relation organizes elements of a set into disjoint groups where every element in a group is related to each other. These groups are called equivalence classes:
```math
[𝓊] = ｛ 𝓋 : 𝓊𝓔𝓋 ｝
```
> - $[a] =｛ b∈A ∣ (a,b)∈𝓔｝$
> All elements in $[a]$ are __equivalent__ to $a$ (under 𝓔).

---


### 📒 Modular Arithmetic**
For example, in modular arithmetic, equivalence classes are defined by remainders:

```math
ℤ/m = \{0,1,2,\ldots,(m-1)\}
```
In modular arithmetic, numbers are grouped into equivalence classes based on a modulus **$m$**. For instance, numbers **$a$** and **$b$** are equivalent modulo **$m$** if they have the same remainder when divided by **$m$**:

```math
a ≡ b \, (\text{mod} \, m) \iff a - b = k·m \, \text{for some} \, k \in ℤ
```
The set of integers modulo **$m$** is denoted **ℤ/m**.

- In **modulo 3** $(ℤ/3)$, the integers are grouped into three equivalence classes based on their remainders when divided by 3:  
  ```math
  \{…,-6,-3,0,3,6,…\}, \{…,-5,-2,1,4,7,…\}, \{…,-4,-1,2,5,8,…\}
  ```
Another example involves real numbers modulo $\tau=2\pi$:
```math
a≡b\,(\text{mod}\,2\pi) ⟺ a = b + k\tau, \text{for } k∈ℤ
```
```
a ≡ b mod 𝟐𝜋 ⟺ ∃k∈ℤ, a = b + k𝜏

ℝ/𝜏 = {r∈(-𝜋,𝜋)} ó {r∈(0,2𝜋)}
```



---
📒 Parallel Lines
- Two lines are equivalent if they are parallel.
```math
L = \{p_a·x + p_b·y + p_0\}, \text{where } p \neq 0.
```
```math
L = \{p_a·x + p_b·y + p_1\}, \text{where } p \neq 0.
```

📒 Multiples
```math
pℤ = { kp | k∈ℤ}
```
---

# 🌌 **Order Relations**

An **order relation** introduces a way to compare elements of a set based on precedence or hierarchy.

### Total vs Partial Order
A relation $𝓡$ on a set $𝕌$ is a **total order** if every pair of elements is comparable:

```math
\text{For all } 𝓊, 𝓋 ∈ 𝕌, \text{either } 𝓊𝓡𝓋 \text{ or } 𝓋𝓡𝓊.
```

A **partial order**, by contrast, does not require all pairs of elements to be comparable.

---

### 📒 **Subset Relation**:
The **subset relation** on sets is an example of a **partial order**:
```math
𝔸 ⊂ 𝔹 \iff \text{every element of } 𝔸 \text{ is also an element of } 𝔹
```

This is $\color{gold}partial$ because, for two sets, $𝔸$ and $𝔹$, it’s possible that neither is a subset of the other.

### 📒 Total Order on Numbers
The standard relation $≤$ on real numbers $ℝ$ is a **total order**:

```math
\text{For all } 𝑥, 𝑦 ∈ ℝ, \text{either } 𝑥 ≤ 𝑦 \text{ or } 𝑦 ≤ 𝑥.
```



--- 
### 📒 **Lexicographic Order**:
A common total order is the **lexicographic order**, often used in dictionaries. For pairs **(𝑟₁, 𝑟₂)** and **(𝑟₁’, 𝑟₂’)** in **ℝ×ℝ**:
```math
(𝑟₁, 𝑟₂) ≼ (𝑟₁’, 𝑟₂’) \iff 𝑟₁ ≺ 𝑟₁’ \, \text{or} \, (𝑟₁ = 𝑟₁’ \text{ and } 𝑟₂ ≼ 𝑟₂’)
```

---

# 🔰 Functions as Relations 

A **function** is a relation between two sets, where each element in the **domain** is mapped to exactly one element in the **codomain**.

```math
𝙵: 𝔸 → 𝔹
```
```math
∀a∈A, ∃!b∈B \text{ such that } F(a)=b.
```
A function $𝙵$ goes from set $𝔸(domain)$ to set $𝔹(codomain)$.
For each element $𝓍$ in $𝔸$, there is a unique element $𝓎$ in $𝔹$ such that $\color{gold}𝓎 = 𝙵(𝓍)$.


- 📒 A function that maps a person to their birth year is an example of a **function** where each person (domain) has a unique birth year (codomain).

#### Inverse Function:
If a function $𝙵$ is invertible, the **inverse** function $𝙵^{-1}$ reverses the mapping:

```math
𝙵^{-1}(𝓎)=\{𝓍∈𝔸 ∣ 𝙵(𝓍)=𝓎\}
```

### **📒 Special Functions**:
- **Identity function**: Maps every element to itself.
- **Constant function**: Maps every element of the domain to the same single element in the codomain.




# 🌌 **Partitions of a Set**

A partition divides a set $𝕌$ into non-overlapping subsets such that:

1. The subsets are pairwise disjoint:

```math
A∩B=∅ \text{ for all } A,B \text{ in the partition.}
```

2. The union of the subsets equals the original set:

```math
⋃A = 𝕌
```

### Relation Between Partitions and Equivalence Relations
Every equivalence relation defines a partition of the set, and conversely, every partition can define an equivalence relation. For $𝓍, 𝓎 ∈ 𝕌$:

```
𝓍𝒬𝓎⟺∃𝔸∊ℙ: {𝓍,𝓎}⊂𝔸
```

### 📒 Partition of Integers
Partition the set of integers into intervals:


```math
ℙ=\{ [i-1,i) ∣ i∈ℤ\}
```
Elements $𝓍$ and $𝓎$ belong to the same subset if they share the same integer part.

---

### 📒 Counting Numbers as a Succession
Consider the **succession relation** defined for the natural numbers, where each number is connected to the next:

```math
0 \to 1 \to 2 \to 3 \to \dots
```

```
ℕ⁰  =
0 → 𝓈(0)  → 𝓈(𝓈(0))    …
0 →   1   →      2     …

a ≤ b ⇔ ∃n : a →ⁿ b | n∊ℕ
```

We define a relation $𝓡$ between two numbers $a$ and $b$ such that:
- $a𝓡b$ if and only if there exists a sequence of steps starting at $a$ that leads to $b$. For example:
  - $0𝓡2$ because $0 \to 1 \to 2$.
  - $1𝓡3$ because $1 \to 2 \to 3$.

This relation is **reflexive, antisymmetric, and transitive**, making it a **total order**:

1. **Reflexive:** Every number is related to itself, as no steps are needed:
```math
   a𝓡a
```
2. **Antisymmetric:** If $a𝓡b$ and $b𝓡a$, then $a = b$, as there cannot be a step "backwards" in succession.

3. **Transitive:** If $a𝓡b$ and $b𝓡c$, then $a𝓡c$, since the steps can be chained together.



---

### Total Order Relations

A relation $𝓡$ is a **total order** if, for any two elements $𝓍$ and $𝓎$:

```math
𝓍𝓡𝓎 \text{ or } 𝓎𝓡𝓍.
```

Total order relations are often denoted using symbols:

- **≼:** Precedes, or antecedent.
- **≽:** Succeeds, or posterior.

In this notation:
```math
a𝓡b \iff a≽b \iff b≼a.
```
> [!NOTE]
> ≺⇔≼∧≠
---

### 📒 Subset Relations
The subset relation is an example of a total order within nested sets:

```math
ℕ⊂ℤ⊂ℚ⊂ℝ.
```

---

### Intervals

Given an ordered set $(𝕌,≼)$, with $a,b∊𝕌$ and $a≼b$, intervals can be defined as follows:

- **Open Interval**:
  ```math
  (a,b) = \{𝓍∈𝕌∣ a≺𝓍≺b\}
  ```

- **Closed Interval**:
  ```math
  [a,b] = \{𝓍∈𝕌∣ a≼𝓍≼b\}
  ```

- **Semi-Open Intervals**:
  ```math
  [a,b) = \{𝓍∈𝕌∣ a≼𝓍≺b\}
  (a,b] = \{𝓍∈𝕌∣ a≺𝓍≼b\}
  ```
---

### Initial and Final Intervals

For an ordered set $(𝕌,≼)$, initial and final intervals can be defined as:

- **Initial Intervals**:
  ```math
  (←,a) = \{𝓍∈𝕌∣ 𝓍≺a\}
  (←,a] = \{𝓍∈𝕌∣ 𝓍≼a\}
  ```

- **Final Intervals**:
  ```math
  (a,→) = \{𝓍∈𝕌∣ 𝓍≻a\}
  [a,→) = \{𝓍∈𝕌∣ 𝓍≽a\}
  ```
---

#### Visualizing Intervals in Succession

Intervals can be defined within this ordered set. For example:
- The closed interval $[1,4]$ includes all numbers between 1 and 4:
  ```math
  [1,4] = \{1, 2, 3, 4\}.
  ```
- An open interval $(1,4)$ excludes the endpoints:
  ```math
  (1,4) = \{2, 3\}.
  ```

In terms of relations:
```math
≺ \iff ≼ \land \neq
```

This ordered structure reflects how natural numbers are connected, and the intervals help visualize subsets of numbers within this succession.



---
### Bounds in Ordered Sets

Given an ordered set $(𝕌,≼)$ and a subset $𝔸⊂𝕌$:

- **Upper Bound**: An element $𝓊$ is an upper bound of $𝔸$ if:
  ```math
  ∃𝓊 : ∀𝓍∈𝔸, 𝓍≼𝓊.
  ```

- **Lower Bound**: An element $𝓊$ is a lower bound of $𝔸$ if:
  ```math
  ∃𝓊 : ∀𝓍∈𝔸, 𝓍≽𝓊.
  ```

If $𝔸$ has both upper and lower bounds, it is called **bounded**.

---

### Bounds in Ordered Sets

Given an ordered set $(𝕌,≼)$ and a subset $𝔸⊂𝕌$:

- **Upper Bound**: An element $𝓊$ is an upper bound of $𝔸$ if:
  ```math
  ∃𝓊 : ∀𝓍∈𝔸, 𝓍≼𝓊.
  ```

- **Lower Bound**: An element $𝓊$ is a lower bound of $𝔸$ if:
  ```math
  ∃𝓊 : ∀𝓍∈𝔸, 𝓍≽𝓊.
  ```

If $𝔸$ has both upper and lower bounds, it is called **bounded**.

- **Maximum**:
  ```math
  Max(𝔸) = M∈𝔸 : ∀𝓍∈𝔸, 𝓍≼M.
  ```

- **Minimum**:
  ```math
  min(𝔸) = m∈𝔸 : ∀𝓍∈𝔸, 𝓍≽m.
  ```

- **Supremum (Least Upper Bound)**:
  The smallest element among all upper bounds, if it exists.

- **Infimum (Greatest Lower Bound)**:
  The largest element among all lower bounds, if it exists.


Máximo, minimo, supremo, ínfimo:
   Únicos 
   



---

### Well-Ordered Sets

A set is **well-ordered**, or a relation $≼$ is a well-ordering, if every non-empty subset has a minimum element. The minimum is often referred to as the "first element of $𝔸$".

---

### Maximal and Minimal Elements

- **Maximal**:
  ```math
  Maxml(𝔸) = M∈𝔸 : ∄𝓍∈𝔸, 𝓍≠M \text{ and } M≼𝓍.
  ```

- **Minimal**:
  ```math
  Minml(𝔸) = m∈𝔸 : ∄𝓍∈𝔸, 𝓍≠m \text{ and } m≽𝓍.
  ```

Maximal and minimal elements coincide with the maximum and minimum if they exist.

---
### Functions Between Sets

A **function** is a relation between two sets where each element of the initial set is related to exactly one element in the final set:

```math
𝙵⊂𝔸×𝔹 \text{ such that } ∀𝓍∈𝔸, ∃!𝓎∈𝔹 : 𝙵(𝓍)=𝓎.
```

In functional notation:

- **Domain**: $𝔸$ (initial set).
- **Codomain**: $𝔹$ (target set).
- **Image**: $𝙵(𝔸)$, the subset of $𝔹$ consisting of outputs of $𝙵$.
- **Inverse Image**:
  ```math
  𝙵⁻¹(𝓎) = \{𝓍∈𝔸 ∣ 𝙵(𝓍)=𝓎\}.
  ```

The set of all functions from $𝔸$ to $𝔹$ is denoted:
```math
𝓕(𝔸,𝔹) \text{ or } 𝔹^{𝔸}.
```






