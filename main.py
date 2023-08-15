import sympy as smp
import math
from IPython.display import display
import numpy as np
x = smp.symbols("x")


class Generator:
    def __init__(self,*args,**kwargs):
        """
        Initialize the generator function for x
        Parameters:
            x: A Symbol object for the x variable
            n[int]: Exponent of the expansion
            a: The a term in (a + bx)^n
            b: The b term in (a + bx)^n
            terms: The number of terms to expand until
        """
        self.x = kwargs.get("x")
        self.n = kwargs.get("n")
        self.a = kwargs.get("a")
        self.b_original = kwargs.get("b")
        self.b = kwargs.get("b") / self.a
        print(self.b)
        
        
        
        self.terms = kwargs.get("terms")
    
    def expand(self):
        if (self.n <= 0) or (type(self.n) != int):
            raise ValueError("n must be a positive integer")
        else:
            return smp.expand(self.a + self.b*x)**self.n
            
    
class BinomialGenerator(Generator):
    def __init__(self,*args,**kwargs):
        #Call the parents init function
        super().__init__(*args,**kwargs)
        self._series = self.generate_series()
        
    def generate_series(self):
        #Declare a variable to store the finished series
        series = 0
        
        for i in range(self.terms):
            #Add the new term into the series
            series += self.calculate_current_term(i)
        #multiply the new series by a^n:
        series *= (self.a**self.n)
        return series
     
    @property
    def binomial_series(self):
        """
        Generate a binomial series expansion with a certain amount of terms for (a + bx)^n where n is negative or a fraction
        """
        return self._series
    
    
    def calculate_current_term(self,i):
        return self.generate_numerator(i)/self.generate_denominator(i)
    
    def generate_numerator(self,i):
        """
        Generate the numerator for the ith term of an expansion
        """
        no_terms_in_numerator = i
        
        if i == 0:
            return 1
        elif i == 1:
            return self.b * self.n * self.x
        else:
            #Generate the numerator
            temp_num = 1
            
            for j in range(i):
                #Keep multiplying terms of (n - i) until you reach the limit
                temp_num *= (self.n - j)
            temp_num *= (self.x ** i) * (self.b ** i)
            return temp_num
    
    @staticmethod
    def generate_denominator(i):
        """
        Generate the denominator for the ith term of an expansion
        """
        return math.factorial(i)
    
    def calculate_validity_range(self):
        """
        Returns the range of validity of a binomial expansion
        """
        if self.b.is_integer() or (type(self.b_original) == int and self.a == 1):
            #If b/a is an integer or a = 1:
            self.validity_range = f"|x| < 1/{abs(self.b)}"
            return f"|x| < 1/{abs(self.b)}"
        else:
            #b/a is not an integer:
            self.validity_range = f"|x| < {abs(1/self.b)}"
            return f"|x| < {abs(1/self.b)}"
    
    @staticmethod
    def solve(exp):
        return smp.solve(exp)
    
    @staticmethod
    def find_validity_range(validity_range):
        return float(validity_range.split("< ")[1])
        
    def approximate_num(self):
        """
        Prompts the user to approximate a number with their binomial expansion.
        """
        import random
        
        #Choose from 2 types of questions - approximate a value close to the expression or estimate a value far from the expression
        q_type = random.choice(["close approx"])
        validity_range = self.find_validity_range(self.calculate_validity_range())
        
        if q_type == "close approx":
            delta_target = round(random.uniform(-1*validity_range,validity_range),2)
            target = self.a + delta_target
            
            exp = self.a + self.b_original * self.x - target #a + bx = target, so a - target + bx = 0
            x_value = self.solve(exp)[0] #Solve a - target + bx = 0
            
            #after we have solved the equation, find the approximation to the target by 
            #subsittuting in the x_value we found into the binomial series
            series = self.binomial_series
            ans = series.subs(x,x_value)
            
            #calculate the actual answer
            real_ans = target ** self.n
            
            #prompt the user for an answer
            print("Q. Find a binomial series approximation for:  ")
            display((self.a + self.b_original*self.x)**self.n)
            print("and use it to approximate (to 3 d.p): ")
            display(smp.Pow(target,self.n,evaluate=False))
            
            user_ans = input("Type your answer: ")
            if(user_ans == round(ans,3)):
                #Correct
                print(f"Your answer was correct! Well done! The actual answer calculated is {real_ans} and the answer approximated by the program is {ans}")
            else:
                #Incorrect
                print(f"Your answer was incorrect! The actual answer calculated is {real_ans} and the answer approximated by the program is {ans}")
            
            
            
    
