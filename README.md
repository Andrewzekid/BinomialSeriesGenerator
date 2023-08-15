# A Fully Functional Python Program to Generate Binomial Series Expansion Problems for Math Practice
Python Code to generate a binomial series approximation question in the form of $`(a+bx)^n`$ where $n$ < 1. 
Built with Python [![My Skills](https://skillicons.dev/icons?i=python)](https://skillicons.dev) and Sympy

```
Q. Find a binomial series approximation for:
$`(x+2)^0.5`$
and use it to approximate (to 3 d.p):
$2.65^0.5$
Type your answer: 1.629
Your answer was incorrect! The actual answer calculated is 1.628 and the answer approximated by the program is 1.628
```

## Features:
- Generate a Binomial Series Representation for $`(a+bx)^n`$ where $n$ < 1.
- Calculate the **range of validity** for this series
- Estimates the value of an expression I.e: $`\sqrt{5}`$ using a binomial expansion and checks the users estimate against it, telling the user if they got it right or not.
- Great math test prep tool! (I used this to practice for my G10 sequences and series test.)

### Usage Instructions
Clone this repository or download and unzip the code. Install sympy, numpy, and IPython.
Open up main.py or create a python file in the same folder and import **`BinomialGenerator`** from main.py: ```from main import BinomialGenerator```

**`BinomialGenerator`** is what we will use to generate a binomial series expansion for $`(a+bx)^n`$

```python
#Import required stuff
from main import BinomialGenerator
import sympy as smp
import math
from IPython.display import display
import numpy as np

#Initialize a symbol in sympy which we will use for printing the binomial series
x_symbol = smp.symbols("x")

#Sample code
generator = BinomialGenerator(x=x_symbol,n=0.5,a=2,b=1,terms=4) #**x** is the sympy symbol we are using to represent x. a,b,n are the a,b,n values in $`(a+bx)^n`$. **terms** is the number of terms of binomial series which we want the program to generate.
#In this case, the program will generate a 4 term binomial series for $`(x+2)^0.5`$.

#Give the user an expression and asks the user to calculate an estimation using binomial series. The program will run its own calculation and check if the users one is correct making for great math practice!!
generator.approximate_num() 

```

Sample Output:
```
Q. Find a binomial series approximation for:
$`(x+2)^0.5`$
and use it to approximate (to 3 d.p):
$2.65^0.5$
Type your answer: 345
Your answer was incorrect! The actual answer calculated is 1.6278820596099706 and the answer approximated by the program is 1.62838543406463
```

If we want to see the binomial expansion that the program generated, we can also run the following:
```
#Prints the binomial series representation calculated by the program
print(self.binomial_series)

#Prints the range of validity for this expansion
print(self.calculate_validity_range())
```
