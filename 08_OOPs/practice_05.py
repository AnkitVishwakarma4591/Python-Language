# Example of multiple Inheritance

class A:
    var_A = "welcome to class A"
    
class B:
    var_B = "welcome to class B"
    
class c(A,B):
    var_c = "welcome to class C"
    
c1  = c()
print(c1.var_A)
print(c1.var_c)
print(c1.var_B)  