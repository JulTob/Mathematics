# 🌌 **The Foundations and Operations of Set Theory**


In our mathematical journey through set theory, we have already explored the vastness of sets, their structures, and the operations that allow us to manipulate them. Now, we delve deeper into the essential foundations and operations that form the core of set theory.



# 🌌 The Essence of Sets



The universe of mathematics is built upon **sets**, denoted by symbols such as:

```math
𝕏, 𝕐, ℤ, 𝔸, 𝔹, ℂ, ℕ, ℝ …
```

A **set** ($𝔸$) is a collection of elements, denoted as ($𝕒ᵢ$), where the **order** of elements is inconsequential. Sets are defined by the criteria that the elements satisfy.


### **Key Principles:**
- **Order**: The arrangement of elements in a set doesn't matter. 
- **Self-containment**: Sets cannot contain themselves as elements, a boundary defined to avoid paradoxes like Russell's Paradox.


To be a proper set, every element ($𝕒ᵢ$) has to be determined to follow some criteria to be in the set ($𝔸$).

For instance, a set **$𝔸$** could contain:
```math
𝕩₀, 𝕩₁, 𝕒₂, 𝕓₃, 𝕚₄, 𝕩₆₅, 𝕨₉₈₇, 𝕣ᵢ...⠀
```

# 🚀 Set Definitions and Comparisons

- **Explicit Definition**: Sets can be defined by **listing** their elements:
  ```math
  𝕃 = \{0, 1\}
  ```

- **Implicit Definition**: Sets can also be described by **properties** that their elements satisfy:
  ```math
  𝔸 = \{ x \mid P(x) \}, \text{ where } P(x) \text{ is a condition for membership}
  ```


### **Set Equality**:
- **Equality**: Two sets are **equal** if they have the **same elements**, regardless of order:
  ```math
  𝔸 = 𝔹 \iff \forall x (x \in 𝔸 \iff x \in 𝔹)
  ```

- **Inequality**: Two sets are **unequal** if they contain **different elements** or some element is absent to the other:
  ```math
  𝔸 ≠ 𝔹 \iff \exists x (x \in 𝔸 \text{ and } x \notin 𝔹)
  ```




## Variables
> 𝕒

In mathematics, a variable represents an element or a collection of elements whose value can vary. Variables serve as placeholders within propositions, allowing for a range of truths depending on their values. The concept of a variable is central to understanding the fluid nature of mathematical statements.

The interplay between elements and sets forms the bedrock of set theory, illuminating the relationship between individual entities and the larger collections they inhabit. Let's delve into these concepts, rendered in the precise language of LaTeX, to explore the essence of variables, set membership, and the philosophical boundaries that define sets.

> A variable $a$ can represent an element or a set of elements within a mathematical proposition, allowing for the exploration of truths across different values.



# Set Membership
```math
𝕒 ∈ 𝔸
```
The notation $𝕒 ∈ 𝔸$ signifies that the element $𝕒$ is a member of the set $𝔸$, a fundamental relationship that connects individual entities to the larger mathematical universe they occupy.

```math
𝚊 \in 𝔸
```
This expression can be interpreted in several ways, emphasizing the multifaceted relationship between elements and sets:
> - $𝚊$ is in $𝔸$
> - $𝚊$ belongs to  $𝔸$
> - $𝚊$ is a member of  $𝔸$
> - $𝚊$ is a point within the collection defined by  $𝔸$

# Non-membership
```math
 𝚊 ∉ 𝔸
```
Conversely, $a∉A$ articulates the absence of $𝚊$ from the set $𝔸$, delineating the boundaries of set membership and the exclusion of specific elements.

```math
𝚊 \notin 𝔸
```
This notation enforces the distinction between inclusion and exclusion within mathematical sets, affirming that:

> - $𝚊$ is not an element of $𝔸$.
> - $𝚊$ is not in $𝔸$.
> - $𝚊$ does not belong to the set $𝔸$.

```math
¬(𝚊∈𝔸)
```

# ***The Set of All Sets*** Paradox

The exploration of sets brings us to a philosophical and logical boundary: the notion that an element cannot be both a set and a member of itself 
```math
¬(𝚊∈𝚊)
```
The conclusion is that the set of all sets does not exist due to the paradoxes such a set would entail.



# 💫 The Void and the Singleton
> $∅$ and $\{ a \}$

The concept of the empty set $∅$, devoid of any elements, introduces the idea of nothingness, while the singleton set $\{ a \}$ illustrates the concept of individuality within set theory.



```math
∅ 
```
Defines the null set, empty.  It contains no elements. 
```math
∅≔ \{ \}
```
```math
∀𝑥,∀𝔸 | 𝑷❨𝑥❩ = 𝑥∉𝔸
```
It is itself a "subset" of any set.

# Singleton $\{ a \}$

> Set of one element


# ⭐ Operations on Sets: Uniting and Intersecting Universes

Set operations, including union ($A∪B$), intersection ($A∩B$), and subtraction ($A−B$), allow us to manipulate and explore the relationships between sets.

# 🌠 Advanced Constructs: Relations and Cartesian Products

The Cartesian Cross Product ($A×B$) and logical relations extend our exploration into the realm of ordered pairs and interactions between sets, offering a new dimension of understanding through the mapping of elements and the formulation of relational structures.

# Conclusion: The Interconnectedness of Set Theory

As we traverse the vast expanse of set theory, from the foundational concepts of sets and their elements to the intricate operations and relationships that bind them, we uncover the mathematical tapestry that underpins the universe of mathematics. This journey reveals the beauty of structure, the elegance of logic, and the profound interconnectedness that lies at the heart of set theory.

Through this exploration, we not only gain a deeper appreciation for the fundamental principles of mathematics but also develop a richer understanding of the cosmic dance of sets and operations that define the mathematical universe. This narrative, woven from the threads of set theory, invites us to continue our exploration, ever seeking the harmonies that define the cosmos of mathematics.



## 𝔸⊂𝔹 

Define que el primer conjunto, a la izquierda, está comprendido por el segundo, a la derecha del símbolo. 

`∀𝑎∊𝔸:｛𝑎∈𝔹｝`


## 𝔸∪𝔹
> ### Unión
<img 
src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Venn0111.svg/1920px-Venn0111.svg.png" 
alt="NN" 
 width="188" 
height="120" 
align="right">

La _suma_ de dos conjuntos se da con el símbolo U, significa reunión.

El conjunto resultante al Unir Pelirrojos o Delgados (unión elemental, añadir los elemento)





## 𝔸∩𝔹
> ### Intersección

<img 
src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Venn0001.svg/1920px-Venn0001.svg.png" 
alt="NN" 
 width="188" 
height="120" 
align="right">

La aplicación de dos propiedades se da con el símbolo ∩ , significa intersección de conjuntos.

El conjunto resultante al seleccionar Pelirrojas y Delgadas (unión determinante, incluir propiedades).

## 𝔸∁, -𝔸, ～𝔸
> ### Complemento
```Ruby
∼A 
∼A ≡ { a | a ∉ A } 
```

## 𝔸-𝔹

<img 
src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Venn0100.svg/1920px-Venn0100.svg.png" 
alt="NN" 
 width="188" 
height="120" 
align="right">

> ### Complemento Relativo

La diferencia entre dos conjuntos se da cómo los elementos del primer conjunto que no estén presentes en el segundo.
```Ruby
 𝔸-𝔹 = {𝑥 | 𝑥∈𝔸, 𝑥∉𝔹}
```


A nivel de lógica:     
```Ruby     
	∩     corresponde con un y            
	U    con un o        
	-      con un y¬ (y no…)          
```

















# Definición de conjuntos 

## Enumeración
Lista de elementos.
Definición por extensión. 

- `𝕃={0,1}`

## Definición

- `{x | P(x)}`

x Satisface la propiedad de P(x)

> The set of all x’s such that P (x) is true. 

```Ruby
{±n | n is a natural number} 
```


## Solución de ecuaciones 



## Descripción 
- {𝑥 | 𝑥∈𝔸}



## Propiedades.
```Python
{𝑥 | 𝑥∈𝑆 y 𝑥 satisface 𝑷}
{𝑥 | 𝑥∈𝑆, 𝑥 : 𝑷(𝑥)}
```























# Comparación de Sets






## 𝔸=𝔹
Tienen los mismos elementos.
- ∀𝚊: 𝚊∈𝔸⟷𝚊∈𝔹




## 𝔸≠𝔹
No tienen los mismos elementos





## 𝔸⊆𝔹
Todos los elementos de 𝔸 están en 𝔹
- ｛2ⁿ｝⊂｛n∙2｝
   
* 𝔸⊆𝔹 ∧ 𝔸⊇𝔹 ⟺ 𝔸=𝔹
   - ∀𝚊 : 𝚊∈𝔸⟶𝚊∈𝔹





# Diagramas de Venn
# ꕢ⧉𖧵⧈⧇⧆





# Propiedades
Propiedades definitorias de pertenencia a un conjunto.



## 𝑷{𝑥}
La variable 𝔁 cumple la propiedad 𝙿




# Predicado
Dado un conjunto 𝔸, un predicado 𝑷  es una propiedad suscrita a 𝑥, un elemento cualquiera del conjunto. 
-  𝔸: universo del predicado.
- 𝑷𝒂𝒓❨1❩ = Falso





## Cuantificadores predicativos (adjetivos)
Los elementos que 
* `𝔸ₚ  = ｛ 𝑥 ∊ 𝔸 ∣ 𝑷❨𝑥❩ ｝`   
Subconjunto de 𝔸 que cumple 𝑷. Such as. Tal que.
   - 𝕊  = ｛ 𝑥∊ ℤ ∣ 𝑥²-𝟹𝑥+𝟸=𝟶｝
   - 𝟚ℕ = ｛𝑛∈ℕ : 𝑛=𝟸𝑚 ∈ℕ｝





## 𝔸:𝑷
- Cualquier predicado sobre 𝔸 define un subconjunto
- Dos predicados son equivalentes cuando determinan el mismo subconjunto. 
    - 𝑷⇔𝑹
- La propiedad 𝑷❨𝑥❩:  𝑥∊𝔸  define un subconjunto 













### Tamaño
```
|𝔸| = n
⇒ |𝓟❨𝔸❩| = 2ⁿ
```










# Operaciones con conjuntos









##  Union 
La unión de conjuntos define como la propiedad de los elementos de pertenecer al menos a un conjunto.
    * 𝔸∪𝔹
    * 𝑥: 𝐴𝑥∨𝐵𝑥
1. 𝔸 ⊂ 𝔸∪𝔹  y 𝔹 ⊂ 𝔸∪𝔹
2. Conmutación 
    * 𝔸∪𝔹 = 𝔹∪𝔸
3. Asociativa
    * 𝔸∪𝔹∪ℂ
4. 𝔸∪∅= 𝔸
5. 𝔸∪𝔸= 𝔸
```Python
⋃ₙ 𝔸ᵢ
```








## Intersección
    * 𝔸∩𝔹
    * 𝑥: 𝐴𝑥∧𝐵𝑥

1. 𝔸∩𝔹 ⊂ 𝔸  𝔸∩𝔹 ⊂ 𝔹
2. Conmutación 
    * 𝔸∩𝔹 = 𝔹∩𝔸
3. Asociativa
    * 𝔸∩𝔹∩ℂ
4. 𝔸∩∅= ∅
5. 𝔸∩𝔸= 𝔸
6. 𝔸∩𝔹 ⊂ 𝔸∪𝔹 
7. Grupos Disjuntos sii
    * 𝔸∩𝔹=∅
    - Ecuaciones incompatibles 
```Python
⋂ₙ 𝔸ᵢ
```









## Distribución 
* 𝔸∩(𝔹∪ℂ)= 𝔸∩𝔹 ∪ 𝔸∩ℂ
* 𝔸∪(𝔹∩ℂ)= 𝔸∪𝔹 ∩ 𝔸∪ℂ











## Diferencia 
* 𝔸-𝔹=𝔸⧵𝔹 
* 𝑥: 𝐴𝑥∧¬𝐵𝑥 
   * 𝔸-𝔹 = 𝔸 -  𝔸∩𝔹
   * 𝔸-𝔹 = 𝔸∩¬𝔹

```Ada
𝓟❨𝕌❩
={ 
∅
𝔸
¬𝔸
𝔹
¬𝔹
𝔸𝔹
𝔸¬𝔹
¬𝔸𝔹
¬𝔸¬𝔹
𝕌
}
```









## Diferencia simétrica 
* 𝔸⩟𝔹 = 𝔸∪𝔹  -  𝔸∩𝔹
    * 𝔸-𝔹 = 𝔸⩟(𝔸∩𝔹)










# Álgebra de conjuntos

## Idempotencia
1. 𝔸⋃𝔸= 𝔸
    1. 𝐴𝑥⋁𝐴𝑥⟺ 𝐴𝑥
2. 𝔸⋂𝔸= 𝔸
    1. 𝐴𝑥⋀𝐴𝑥⟺ 𝐴𝑥



## Conmutación 
1. 𝔸⋃𝔹 = 𝔹⋃𝔸
    1. 𝐴𝑥⋁𝐵𝑥 ⟺ 𝐵𝑥⋁𝐴𝑥
2. 𝔸⋂𝔸= 𝔹⋂𝔸
    1. 𝐴𝑥⋀𝐵𝑥 ⟺ 𝐵𝑥⋀𝐴𝑥




## Asociativas
1. 𝔸⋃𝔹⋃ℂ
    1. 𝐴𝑥⋁𝐵𝑥⋁𝑪𝑥
2. 𝔸⋂𝔹⋂ℂ
    1. 𝐴𝑥⋀𝐵𝑥⋀𝑪𝑥





## Distributivas
1. (𝔸⋃𝔹)⋂ℂ= 𝔸⋂ℂ ⋃ 𝔹⋂ℂ
    1. (𝐴𝑥⋁𝐵𝑥)⋀𝑪𝑥 ⟺ 𝐴𝑥⋀𝑪𝑥 ⋁ 𝐵𝑥⋀𝑪𝑥
2. (𝔸⋂𝔹)⋃ℂ= 𝔸⋃ℂ ⋂ 𝔹⋃ℂ
    1. (𝐴𝑥⋀𝐵𝑥)⋁𝑪𝑥 ⟺ 𝐴𝑥⋁𝑪𝑥 ⋀ 𝐵𝑥⋁𝑪𝑥






## Identidad
1. 𝔸⋃∅=𝔸
    1. 𝐴𝑥⋁𝟎 ⟺ 𝐴𝑥
2. 𝔸⋃𝕌=𝕌
    1. 𝐴𝑥⋁𝟏 ⟺ 𝟏
3. 𝔸⋂∅=∅
    1. 𝐴𝑥⋀𝟎 ⟺ 𝟎 
4. 𝔸⋂𝕌=𝔸
    1. 𝐴𝑥⋀𝟏 ⟺ 𝐴𝑥





## Complemento
1. 𝔸⋃𝔸͞ = 𝕌
    1. 𝐴𝑥⋁¬𝐴𝑥⟺ 𝟏
2. 𝔸⋂𝔸͞ = ∅
    1. 𝐴𝑥⋀¬𝐴𝑥⟺ 𝟎
3. 𝔸͞͞ = 𝔸
    1. ¬¬𝐴𝑥⟺ 𝐴𝑥
4. 𝕌͞ = ∅
    1. ¬𝟏 ⟺ 𝟎
5. ∅͞ = 𝕌
    1. ¬𝟎 ⟺ 𝟏





## De Morgan 
1. ¬(𝔸⋃𝔹) = ¬𝔸⋂¬𝔹
    1. ¬(𝐴𝑥⋁𝐵𝑥)⟺ ¬𝐴𝑥⋀¬𝐵𝑥
3. ¬(𝔸⋂𝔹) = ¬𝔸⋃¬𝔹
    1. ¬(𝐴𝑥⋀𝐵𝑥)⟺ ¬𝐴𝑥⋁¬𝐵𝑥






## Producto de dos conjuntos 


### Vector: Producto cartesiano, Par ordenado
```Ada
𝔸×𝔹= {
   (𝒙,𝒚) ∣  𝒙∊𝔸, 𝒚∊𝔹 }

𝔸²= 𝔸×𝔸= {
   (𝒙,𝒚) ∣  𝒙,𝒚 ∊𝔸}

ℝ²: Plano Cartesiano

𝔸×𝔹 ≠ 𝔹×𝔸

𝔸₁×𝔸₂×···×𝔸ₙ
𝔸ⁿ : Nuplas, N-Vector
  ={ (𝑎₁,𝑎₂,...,𝑎ₙ) | 𝑎ᵢ∈𝔸 }
```







#  Relación Lógica 
```Ada
𝒜
   = {(𝒙,𝒚) ∣ 𝒙∊𝔸, 𝒚∊𝔹 : 𝐴𝑥𝑦 }

𝒜 es un grafo de la relación lógica, o correspondencia.

𝒜 : 𝔸⟶𝔹
   𝔸: conjunto inicial
   𝔹: conjunto final
      𝒙𝒜𝑦   𝒙 está relacionado con 𝑦
          𝒙𝒜̸𝑦   No está relacionado.
```

Ejemplo:
```Ada
𝔸={0,1,2} = 𝔹
𝒙𝒜𝑦 : 𝒙 menor que 𝑦

𝒜={ (0,1),(0,2),(1,2)}
  0𝒜1,0𝒜2,1𝒜2,
  0𝒜̸0, 1𝒜̸0, 2𝒜̸0, 1𝒜̸1, 2𝒜̸1, 2𝒜̸2
```Ada






## Inversa
```Ada
𝒜⁻¹
   = {    (𝒚,𝒙) ∈ 𝔹×𝔸  : 𝒜   }
```

Ejemplo
```Ada
Del anterior
𝒜⁻¹ ={ (1,0),(2,0),2,1) }
```





# Composición 
```Ada
𝒜∘ℬ
   = 𝑥𝒜𝑦ℬ𝑧 = 𝑥𝒜𝑦 ⋃ 𝑦ℬ𝑧
```






# Lógica Relacional
```Ada
∀𝑥∊𝔸,∀𝑦∊𝔹: 𝒜𝑥𝑦
∃𝑥∊𝔸,∀𝑦∊𝔹: 𝒜𝑥𝑦
∃𝑥∊𝔸,∃𝑦∊𝔹: 𝒜𝑥𝑦
```


# G. Cantor
1. Un conjunto queda definido por una propiedad. 
2. Un conjunto es una identidad matemática, puede ser un elemento.
3. Dos conjuntos con los mismos elementos son iguales

Escuela 1: G. Frege, B. Russell, E. Zermelo, A. Fraenkel

Escuela 2: von Newman, Bernay, Gödel 

## Teoría de Conjuntos de ZF
Axiomas:
1. Extensión: ∀𝑥 : [ 𝑥∈𝔸⟷𝑥∈𝔹]⟶𝔸=𝔹
2. Conjunto Vacío: ∃∅ : ∀𝑥(𝑥∉∅)
3. Pares: ∀𝔸,𝔹 ∃ℂ : ∀𝑥[ 𝑥∈ℂ⟷(𝑥=𝔸⋁𝑥=𝔹)]
4. Unión: ∀ℂ ∃𝕊 ∀𝑥 : [ 𝑥∈𝕊⟷∃𝔸:(𝔸∈ℂ⋀𝑥∈𝔸)]
5. Conjunto de Potencia: 𝓟❨ℂ❩
    1. ∀ℂ ∃𝓟❨𝔸❩ ∀𝔹:
        1. 𝔹∈ 𝓟❨𝔸❩⟷∀𝑥:
            1. 𝑥∈𝔹⟶𝑥∈𝔸
6. Especificación:
    1. 𝒇(𝑡)
    2. ∀𝔸 ∃𝔹 ∀𝑥 :
        1. 𝑥∈𝔹⟷𝑥∈𝔸⋀ 𝒇(𝑥)
7. Sustitución:
    1. 𝒇(𝑡,𝑣)
    2. 𝑥∈𝔸
    3. 𝔹={𝑦| 𝒇(𝑥,𝑦)}
    4. 𝒇: 𝔸⟶𝔹
    5. : 𝒇(𝔸)=𝔹
8. Infinitud
    1. ∃𝔸 :
        1. ∅∈𝔸
        * ⋀
        1. ∀𝑥 𝑥∈𝔸⟶𝑥⋃{𝑥}∈𝔸
9. Regularidad:
    1. ∀𝔸 :
        1. 𝔸≠∅ ⟶∃𝔹:
            1. 𝔸⋂𝔹=∅

## Paradoja de Cantor
1. ∃ℂ:(∀𝕊ⅇ𝕥∈ℂ)
2. ℂ∈𝓟❨ℂ❩
3. ⟶ 𝓟❨ℂ❩∈ℂ
4. ℂ= 𝓟❨ℂ❩     ☒


## Paradoja de Russel
1. Sea 𝕄 el conjunto de conjuntos que no son elementos de sí mismos.
1. 𝕄={𝕏|𝕏∉𝕏}
1. ¿Es 𝕄 un elemento de sí mismo?






# Equivalence

Let 𝔸 be a set.

A relation on 𝔸 is a comparison test 
between members of ordered pairs of elements of 𝔸. 
If the pair (𝑎, 𝑏) ∈ 𝔸 × 𝔸 passes this test, we write 
`𝑎 ◃ 𝑏`
and read “a is related to b”. An equivalence relation
 on 𝔸 is a relation that has the following properties: 

- Reflexivity
  - `𝑎 ◃ 𝑎`	   	
- Symmetry
  - `𝑎◃𝑏 ⟺ 𝑏◃𝑎`	
- Transitivity 
  - `a◃b`  
  - `b◃c` 
     - `⇒ a◃c`



The set [[𝑎]] = {𝑏 ∈ 𝔸 | 𝑏 ◃ 𝑎} 
of all elements that are equivalent to 𝑎 is called the equivalence class of 𝑎. 

 

# Predicados
# Operaciones con conjuntos
# Algebra de Boole
# Producto cartesiano
# Relaciones



# Set Operations

Set operations are the tools that allow us to navigate the vast and complex cosmos of mathematics, combining, intersecting, and differentiating sets in a manner that reveals the underlying structure of the mathematical universe. 

# 🌌 The Universal Set

At the foundation of our cosmic exploration is the Universal Set, denoted as $U$. This set is the mathematical universe itself, encompassing all the elements under consideration. The _`Universal`_ set is what we **define** to be the universal set, contextually. The Universal Set contains all the elements we are interested in.

Every set within our discussion is a subset of this universal domain, much like how every star, planet, and galaxy exists within the star system, the galaxy, and the universe itself.

```math
\text{Let } U \text{ be the universal set, then for any set } A, \, A \subseteq U.
```





# 🚀  Overlap

In sets, two fundamental interaction exist: Intersection and Union.



# Intersection (∩)


<img 
src="https://www.tutorialspoint.com/fuzzy_logic/images/intersection_operation.jpg"
alt="Intersection" 
 width="144" 
align="right">

When sets overlap, sharing common elements, their intersection is the set of all elements they have in common. The intersection of sets $A$ and $B$ is denoted as $A ∩ B$.

The set of all overlapping elements. 

```math
A \cap B = \{x \mid x \in A \text{ and } x \in B\}
```

If the intersection is empty $(𝔸∩𝔹＝∅)$, then the sets are ___disjoint___.
If the intersection is not empty $(𝔸∩𝔹≠∅)$, then the sets ___intersect___.







# Union (∪)
The union of sets combines all elements from each set, creating a new set that contains every element from both, without duplicates. The union of sets $A$ and $B$ is denoted as $A ∪ B$.

<img 
src="https://www.tutorialspoint.com/fuzzy_logic/images/union_operation.jpg"
alt="Intersection" 
 width="144" 
align="right">

The set of all elements in either group. 

```math
A \cup B = \{x \mid x \in A \text{ or } x \in B\}
```
 




# 💫 Subtraction and Complement: Defining the Other

<img 
src="https://www.tutorialspoint.com/fuzzy_logic/images/relative_complement_operation.jpg"
alt="Intersection" 
width="273" 
align="right">

Beyond the realms of union and intersection lie the concepts of Subtraction and Complement, operations that define what remains when we exclude certain elements.

# Subtraction (−)
The subtraction of set $B$ from set $A$ (denoted $A - B$) leaves us with a set containing only those elements of $A$ that are not in $B$.

The Subtraction of B from A is the set after taking away from A all the elements in B.
```math
A - B = A \setminus B = \{x \mid x \in A \text{ and } x \notin B\}

```

# Complement

<img 
src="https://www.tutorialspoint.com/fuzzy_logic/images/complement_of_set.jpg"
alt="Intersection" 
width="189" 
align="right">

The complement of a set $A$ within the universal set $U$ consists of all elements in $U$ that are not in $A$. It represents the "outside" of $A$ in the universe.


```math
A̅ = U - A
```
```math
\bar{A} = ¬A = A∁ = U - A = \{x \mid x \in U \text{ and } x \notin A\}
```



# ⭐ Properties of Set Operations

Set operations adhere to several foundational properties that govern their behaviour.


### Commutative
- $A∪B=B∪A$
- $A∩B=B∩A$

### Associative
- $A∪(B∪C)=(A∪B)∪C$
- $A∩(B∩C)=(A∩B)∩C$

### Distributive
- $A∪(B∩C)=(A∪B)∩(A∪C)$
- $A∩(B∪C)=(A∩B)∪(A∩C)$


###  Idempotency
- $A∪A=A$
- $A∩A=A$

### Identity
- $A ∪ ∅ = A$
- $A ∩ U = A$
- $A ∩ ∅ = ∅$
- $A ∪ U = U$

### Transitive
- $If A ⊆ B ⊆ C$, then $A ⊆ C$

### Involution
- $¬¬A = A$

###   De Morgan
- $¬(A∩B) = ¬A ∪ ¬B$
- $¬(A∪B) = ¬A ∩ ¬B$



# Cartesian Cross Product

The Cartesian Cross Product expands our horizons, creating pairs from elements of two sets that illuminate the relationships between them, much like charting coordinates in space.
```math
A \times B = \{(a, b) \mid a \in A, b \in B\}

```
```Ada
A × B = {
{a1,b1}, {a2,b1}, {a3,b1}, ---
{a1,b2}, {a2,b2}, ---
{a1,b3}, ---
---
```

Set operations are the fabric through which the universe of mathematics is woven, allowing us to explore the relationships between sets in a structured and meaningful way. Through these operations, we unveil the interconnectedness of all mathematical concepts, reflecting the intricate and boundless nature of the cosmos itself.

# 💥 Power Set 

A power set is the set of all possible subsets of a given set, including the empty set and the set itself.

Example:

If $  A = \{1, 2\} $￼, then the power set of $A$￼, denoted as  $\mathcal{P}(A)$ ￼, is:

```math

\mathcal{P}(A) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}

```
> [!IMPORTANT]
> * If a set $A$ ￼ has $n$￼ elements, the power set will have $2^n$￼ subsets.
> * The smallest power set is $\mathcal{P}(∅) = \{∅}$￼.

It’s essentially like listing every combination of the elements in the original set.

---
# Famous Sets
### ℕ Natural Numbers 
### ℤ Integers
### ℚ Rationals 
### ℝ Reals
### ℂ Complex
### Modifiers:
- $S^{*}$: S except 0
- $S^{+}$: S non-negatives.
- $S^{>0}$: S Strictly positives.
### Intervals
Certainly! Here's a concise explanation:

---

### 🌈 **Intervals as Sets**

Intervals in mathematics are **sets** that contain all numbers between two endpoints, often representing a continuous range of values. Each interval is defined by the properties of its boundaries:

1. **Closed Interval** $[a, b]$: Includes the endpoints $a$ and $b$, as well as all numbers in between.
   - Example: $[1, 3] = \{x : 1 \leq x \leq 3\}$.

2. **Open Interval** $(a, b)$: Includes all numbers between $a$ and $b$, but excludes the endpoints.
   - Example: $(1, 3) = \{x : 1 < x < 3\}$.

3. **Half-Open Intervals** $[a, b)$ or $(a, b]$: Include only one endpoint.
   - Example: $[1, 3) = \{x : 1 \leq x < 3\}$.

Intervals are perfect examples of sets because they collect **all numbers** that satisfy a given condition: being between $a$ and $b$. 


  
