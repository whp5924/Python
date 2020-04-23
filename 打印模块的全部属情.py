#
import urllib
def print_all(module_):
    modulelist = dir(module_)
    print(modulelist)
    length = len(modulelist)
    for i in range(0, length, 1):
         print(modulelist[i])
         print(getattr(module_, modulelist[i]),end='')

print_all(urllib)
