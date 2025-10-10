Linear Program:

min $x_1 - 2x_2 + x_4$

* subject to:  
   *  $x_1 - x_3 ≤ 3$
   *  $x_2 + x_4 ≥ 2$
   *  $x_1 + x_2 = 4$
   - $x_1 , x_2, x_3, x_4 ≥ 0$

1. We can make the following observations:
   1. $x_2 = 4 - x_1$

2. We can standarize using slack variables:
   *  $x_1 - x_3 + s_1 = 3$
   *  $x_2 + x_4 = 2 + s_2$
   *  $x_1 + x_2 = 4$
   *  min $x_1 - 2x_2 + x_4$

   or, using $x_2 = 4 - x_1$:

   *  $x_1  - x_3  + s_1 = 3$
   *  $x_1  - x_4  + s_2 = 2 $
   *  min $ - 8 + 3x_1 + x_4$

3. Therefor we have the simplex tableau for


| $s_1$ |  $3 - x_1  + x_3$ | 3 |
|--|--|--|
| $s_2$ |  $2 - x_1  + x_4$ | 2 |
| min    | $- 8 + 3x_1 + x_4$ | -8 |

where we select $x_1$ as pibot, and as the ratio of both entries is -3, we choose the top one by order.


