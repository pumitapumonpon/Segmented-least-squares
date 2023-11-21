# Segmented-least-squares
This code is an implementation of Segmented least squares using Matplotlib to display the results.

It's classic problem in statistics and numerical analysis:
    Given n points in the plane $(x_{1}, y_{1}), (x_{2}, y_{2}), \ldots , (x_{n}, y_{n}) $
    find a line $y = ax + b$ such that the mean square error is minimized.

  $$SSE = \sum_{i=1}^{n} (y = ax + b)^{2}$$

  and the error is minimized when

  $$a = fracc{n \sum_{i} x_{i}y_{i} - (\sum_{i} x_{i})(\sum_{i} y_{i})}{n \sum_{i} x_{i}^{2} - (\sum_{i} x_{i})^{2}},$$
    
  $$b = fracc{\sum_{i} y_{i} - a \sum_{i}x_{i} }{n}$$

    
  Given that n points in the plane $(x_{1}, y_{1}), (x_{2}, y_{2}), \ldots , (x_{n}, y_{n})$
  with $x_{1} < x_{2} < \ldots < x_{n}$, find a sequence of lines such that it is minimized.
    
  *The sum of errors $E$ in each line segment
  *The number of lines $L$
  *Then the function to optimize is $f(x)= E + c * L$, for some constant $c$
  *$OPT(j)$ is the minimum cost for points $p_{1}, p_{i+1}, \ldots , p_{j}.$
  *$e(i,j)$ is the sum of the errors for the points $p_{1}, p_{i+1}, \ldots , p_{j}.$
    - To $j = 0$, $OPT(j) = 0$
    - Otherwise $OPT(j) = min_{1 <= i <= j} \{ e(i,j) + c + OPT(i-1)\}$

References:
  Notes of the class
