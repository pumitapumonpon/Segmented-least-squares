# Segmented-least-squares

This code is an implementation of Segmented least squares using Matplotlib to display the results.

It's a classic problem in statistics and numerical analysis: Given n points in the plane \((x_{1}, y_{1}), (x_{2}, y_{2}), \ldots , (x_{n}, y_{n})\),
find a line \(y = ax + b\) such that the mean square error is minimized.

The mean square error (SSE) is given by:

\[SSE = \sum_{i=1}^{n} (y_i - (ax_i + b))^2\]

The coefficients \(a\) and \(b\) are minimized when:

\[a = \frac{n \sum_{i} x_{i}y_{i} - (\sum_{i} x_{i})(\sum_{i} y_{i})}{n \sum_{i} x_{i}^{2} - (\sum_{i} x_{i})^{2}}\]

\[b = \frac{\sum_{i} y_{i} - a \sum_{i}x_{i} }{n}\]

Given that there are \(n\) points in the plane \((x_{1}, y_{1}), (x_{2}, y_{2}), \ldots , (x_{n}, y_{n})\)
with \(x_{1} < x_{2} < \ldots < x_{n}\), the goal is to find a sequence of lines such that it is minimized.

+ The sum of errors \(E\) in each line segment
+ The number of lines \(L\)
+ Then the function to optimize is \(f(x) = E + c \cdot L\), for some constant \(c\)
+ \(OPT(j)\) is the minimum cost for points \(p_{1}, p_{i+1}, \ldots , p_{j}.\)
+ \(e(i,j)\) is the sum of the errors for the points \(p_{1}, p_{i+1}, \ldots , p_{j}.\)
  - To \(j = 0\), \(OPT(j) = 0\)
  - Otherwise \(OPT(j) = \min_{1 \leq i \leq j} \{ e(i,j) + c + OPT(i-1)\}\)

References:
Notes of the class

