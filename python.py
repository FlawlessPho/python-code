def function_1(x,y):
# command can be turned into a function as shown reducing num of lines
#    x = 5
#    y = 8
    z = x + y
    print(z)
function_1(5,8)

def function_2(x,y):
#    x = 7
#    y = 43
    z = x + y
    print(z)
function_2(7,43)

def function_3(function_1,function_2):
    a = function_1 * function_2
    print(a)
   function_3(function_1(x,y), function_2(x,y))
