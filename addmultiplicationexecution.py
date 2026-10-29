#MODULES AND PACKAGES
'''MODULES:- collection of function.
   PACKAGES:- collecton of MODULES.'''

'''import addmultiplication
print(addmultiplication.x)
addmultiplication.sum(1,2)
addmultiplication.multiplication(2,3)
addmultiplication.sub(4,3)

import addmultiplication as ponk
print(ponk.x)
ponk.sum(1,2)
ponk.multiplication(2,3)
ponk.sub(4,3)

from addmultiplication import * #imports everything
print(x)
sum(13,5)
sub(5,2)'''

'''from addmultiplication import x as x, sum as add, sub as min #aliases for member in the module
x=20
print(x)
min(12,5)
add(2,5)'''

#RELOAD:- If a module being utilize is updated, those updates are not booted up until and unless we use RELOAD.

#dir:- lists out all the members of the current module
# dir(moduleName):- specified module

'''import addmultiplication
print(dir) 
print(dir(addmultiplication))'''

'''import my_package.addmultiplication
print(dir(my_package))'''

#any folder possessing a file named __init__.py becomes a pavkage





