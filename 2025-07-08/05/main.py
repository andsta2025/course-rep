def method_call_counter(cls):
    """
    A class decorator that counts how many times any method of the class is called.
    """
    class WrappedClass(cls):
        _method_call_count = 0  # class-level counter
        def __getattribute__(self, name):
            attr = super().__getattribute__(name)
            if callable(attr) and not name.startswith("_"):  # exclude special/private methods
                def new_func(*args, **kwargs):
                    WrappedClass._method_call_count += 1
                    print(f"Method '{name}' called. Total calls: {WrappedClass._method_call_count}")
                    return attr(*args, **kwargs)
                return new_func
            return attr

    return WrappedClass

# Example usage:
@method_call_counter
class MyClass:
    def foo(self):
        print("foo called")

    def bar(self):
        print("bar called")

if __name__ == "__main__":
    obj = MyClass()
    obj.foo()
    obj.bar()
    obj.foo()  
    obj.foo()
    
    # Calling foo again to see the counter increment
    print(f"Total method calls: {MyClass._method_call_count}")
    # This will print the total number of method calls made on the class
 