from stack import Stack
import better_exceptions

def calculate(s):
    ops = ["+", "-", "*"]
    nums = ["1","2","3","4","5","6","7","8","9","0"]
    ops_stack = Stack()
    nums_stack = Stack()
    s = list(s)
    print(s)
    for i in s:
        print(type(i))
        if i in ops:
            ops_stack.push(i)
        elif i in nums:
            nums_stack.push(i)
        elif i==")":
            num2 = nums_stack.pop()
            num1 = nums_stack.pop()
            op = ops_stack.pop()
            result = str(num1)+op+str(num2)
            nums_stack.push(eval(result))
    return nums_stack.pop()



if __name__=="__main__":
    s = "((1+((2+3)*(4*5)))+(4-3))"
    print(calculate(s))
            
    
