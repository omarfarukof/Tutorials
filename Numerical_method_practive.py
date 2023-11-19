from Numerical_Methods.methods import *
import numpy as np
import sympy as sp

f = lambda v: 0.01*v**7 + 0.05*v**5 + 0.1*v**3 + 2*v - 2
f_dif = lambda v: 7*0.01*v**6 + 5*0.05*v**4 + 3*0.1*v**2 + 2


# print( np.abs(1 - 2) )
# vari = sp.symbols('v')
# if check_func(vari , sym=True):
#     print( "vari is a symple" )
#     print(vari)
# f_2 = 0.01*v**7 + 0.05*v**5 + 0.1*v**3 + 2*v - 2

# f_v = lambda2sym(f , symble='v')
# print(f_v)
# print(f_v.subs(v,0))
# f_2 = sp.lambdify(v ,f_2)
# print(f_2(0))
# # print(f_2(0))

def print_nm_details(solve = None , heading = False , tab_str="\t "):
    if heading:
        print("Numerical Methods" , "\t|", "Iter" ,"\t|", "Solution" , "\n","-"*50)
    else:
        if len(solve.method) < 15:
            tab_str = "\t\t "
        print(solve.method , tab_str, solve.max_iteration ,"\t ", solve.root)


print_nm_details(heading=True)

solve = bisection_method( f , 0 , 1 , significant_digit=6 , analysis=True)
print_nm_details(solve)

solve = false_position_method( f , 0 , 1 , significant_digit=6 , analysis=True )
print_nm_details(solve)

vari = sp.symbols('v')
# g = ( lambda2sym(f , vari) - 2*vari ) / (-2)
g =lambda v: (.01*v**7 + 0.05*v**5 + 0.1*v**3 - 2) / (-2)
# g = lambda v: 0.01*v**7 + 0.05*v**5 + 0.1*v**3 + 2*v - 2 + v

solve = fixed_point_iteration(g , 'v' , 1 , gofx_format=True , significant_digit=6 , analysis=True)
print_nm_details(solve)

solve = newton_raphson_method(f , 'v' , 1 , significant_digit=6 , analysis=True)
print_nm_details(solve)

# x_new = 1
# print("function of",x_new ,"=", f(x_new))


solve = secand_method(lambda2sym(f , 'v') , 'v' , 0 , 1 , significant_digit=6 , analysis=True )
print_nm_details(solve)

solve = modified_secand_method( lambda2sym(f , 'v') , 'v' , 1 , significant_digit=6 , analysis=True )
print_nm_details(solve)