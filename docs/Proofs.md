# 🐣 How to self-explain
🐥 To improve your understanding of a proof, there is a series of techniques
you should apply.     

- 🦉 After reading each line:
  * 🦚 Try to identify and elaborate the main ideas in the proof.
  * 🪿 Attempt to explain each line in terms of previous ideas. These may be ideas from the information in the proof, ideas from previous theorems/proofs,
or ideas from your own prior knowledge of the topic area.
  * 🦢 Consider any questions that arise if new information contradicts your
current understanding.
Before proceeding to the next line of the proof you should ask yourself
the following:
* 🦆 Do I understand the ideas used in that line? 
* 🦩 Do I understand why those ideas have been used?
* 🐓 How do those ideas link to other ideas in the proof, other theorems, or
prior knowledge that I may have?
* 🦤 Does the self-explanation I have generated help to answer the questions
that I am asking?
🐦‍🔥 By engaging in self-explanation, you deepen your understanding and ensure that every step in a proof is clear and justified.



# The Philosophy of Proofs

[<img 
src="https://img.youtube.com/vi/xoKozKnzq3I/maxresdefault.jpg"
alt="Maths" 
width = 300
align="right">](https://youtu.be/xoKozKnzq3I)

The most important thing about proofs is that they are precise descriptions of the though process for a statement's rationalization. 

It is tradition to finish proofs with the latin words: "Quod erat demonstradum", or the abrebiation $QED$

# 🌬️ Induction & Proof Techniques

### 💧 Mathematical Induction
- 💧 Prove formulas for sums, or recursion patterns.
### ☔️ Proof by Contradiction, Construction, etc.
- ☔️ “A rope-and-nails” style logic puzzle, “infinite descent.”



# Proofs

[<img 
src="https://img.youtube.com/vi/Ol5BoUV6SjA/0.jpg"
alt="Maths" 
width = 300
align="right">](https://youtu.be/Ol5BoUV6SjA)

> Prove only the things that are true 

A **proof** is a valid argument that establishes the truth of a _mathematical statement_. 

A proof can use the _**hypotheses**_ of the theorem, if any, _**axioms**_ assumed to be true, and previously proven theorems. 

Using these ingredients and rules of inference, the final step of the proof **establishes the truth of the statement** being proved. 

[<img 
src="https://img.youtube.com/vi/ua-OJVY1id8/0.jpg"
alt="Maths" 
width = 300
align="right">](https://youtu.be/ua-OJVY1id8)


A **theorem** is a statement that can be shown to be true 

Less important theorems sometimes are called _propositions_. 

Theorems can also be referred to as _facts_ or _results_. 

**We demonstrate that a theorem is true with a proof.**

A proof is a **valid argument** that establishes the truth of a theorem. 

[<img 
src="https://img.youtube.com/vi/oQHrVATWDts/0.jpg"
alt="Maths" 
width = 300
align="right">](https://youtu.be/oQHrVATWDts)

The statements used in a proof can include **axioms (or postulates)**, which are statements we _assume to be true_.

A less important theorem that is helpful in the proof of other results is called a **lemma** (plural _lemmas or lemmata_). 

A **corollary** is a theorem that can be established directly from a theorem that has been proved. 

A **conjecture** is a statement that is being proposed to be a true statement, usually on the basis of some partial evidence, a heuristic argument, or the intuition of an expert. 

When a proof of a conjecture is found, the conjecture becomes a theorem. 

[<img 
src="https://img.youtube.com/vi/iNACH6Fkdrs/0.jpg"
alt="Maths" 
width = 300
align="right">](https://youtu.be/iNACH6Fkdrs)



----
# 📍 DIRECT PROOF: 

### The square of an odd integer is odd.
1. Let $𝚗∈ℕ$
2. Then $n$ is 1 more than an even integer, so $\color{gold}n = 1 + 2m$ for some integer $m$.  
   1. $n^2$ = $(1+2m)^2$
   2. $n^2$ = $(1+2m)(1+2m)$ = $1 + 4m +4m^2$ = $1 + 4(m+m^2)$
3. This is 1 more than $\color{orange}4(m + m^2)$, an even number.   
$\color{gold}∴ n^2 \text{ is odd.}$
```math
\color{gold}
∎ n: \text{ odd} ⟹ n^2: \text{ odd, } n^2 = 1+4k \;\;(k∈ℕ)
```
This is a $\color{gold}DIRECT$ proof.

### The square of a multiple of 3 is also multiple of 3
1. Let $𝚗∈ℕ$
2. Then $n∷3$, so $\color{gold}n = 3m$ for some integer $m$.  
   1. $n^2$ = $(3m)^2$
   2. $n^2$ = $9·m^2$ 
3. 9 is multiple of 3. $3∣9$     
$\color{gold}∴ n^2 \text{ is multiple of 3.}$
```math
\color{gold}
∎ n: 3 ∣ n ⟹ n^2: \left\{\begin{matrix} 3 ∣ n^2, \\ 9 ∣ n^2 \end{matrix}\right.
```

***

# PROOF BY CONTRADICTION

### No real number has square equal to −1
1. Suppose the statement is false. This means that there is a real number, say $x$, such that $\color{gold}x: x∈ℝ, x^2 =−1$. 
2. A property of real numbers is that $\color{lime}∀r∊ℝ : r^2 ≥ 0$
3. $x$ is a real number, so $x:$ $\color{gold}x^2 = -1$ AND $\color{lime}x^2≥ 0$
4. `3` Is a contradiction. `1` must be false
5. ∴ No real number has square equal to −1
- ∎


















