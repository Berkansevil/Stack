

class stack(object):
    def __init__(self,limit=10):
        self.stk=[]
        self.limit=limit
    def isempty(self):
        return len(self.stk)<=0
    def push(self,item):
        if len(self.stk)>=self.limit:
            print("stack overflow")        
        else:
            self.stk.append(item)
            print("stack after push",self.stk)
    def pop(self):
        if len(self.stk)<=0:
            print("stack Underflow")
            return 0
        else:
            return self.stk.pop()    
    def peek(self):
        if len(self.stk) <=0:
            print("stack owerflow")        
            return 0
        else:
            return self.stk[-1]
    def size(self):
        return len(self.stk)    

our_stack=stack(5)
our_stack.push("1")
our_stack.push("21")            
our_stack.push("40")            
our_stack.push("51")            
our_stack.push("54") 
our_stack.push("95") 
our_stack.push("67") 
our_stack.push("90") 

print(our_stack.peek())
print(our_stack.pop())
print(our_stack.peek())
print(our_stack.pop())