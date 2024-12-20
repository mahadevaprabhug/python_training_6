"""
Variable Scopes
1. Local Scope
2. Enclosed Scope
3. Global Scope
4. Builtin Scope
"""
print("1. Local Scope")
print("-"*20)
# --------------

def my_function():
    a = 100 # Local Scope, We can't access outside

print("#"*40, end="\n\n")
################################

print("2. Enclosed Scope")
print("-"*20)
# --------------

def my_outer_function():
    x = 10 # Enclosed Scope: current & nested function can access
    def my_nested_function():
        print("We can access here:", x) # outer function variable

print("#"*40, end="\n\n")
################################

print("3. Global Scope")
print("-"*20)
# --------------

z = 100
def my_outer_function():
    print("z:", z) # global scope
    def my_nested_function():
        print("z:", z) # global scope

# print("z:", z) # global scope

print("#"*40, end="\n\n")
################################

# If nowhere if that variable present then
# at last it will check in builtins
