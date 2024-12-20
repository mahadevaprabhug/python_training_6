"""
Frozenset:
        -- To keep multiple values like list of employee names
        -- We can keep unique values
        -- index number will not be there for each value
"""
print("Frozenset PART-1")
print("Store values")
print("-"*20)
# --------------

# Frozenset: we dont have shorcut, we need to use class name
my_fs = frozenset([10, 10, 10, "python", "python", "java", "java"])
print(my_fs)

# If we want index then convert to other type like list/tuple etc
# L = tuple(my_fs)
# OR we can use any loops to iterate

print("#"*40, end="\n\n")
################################

print("Frozenset PART-2")
print("Methods present inside 'frozenset' class")
print("-"*20)
# --------------

print(dir(frozenset))

print("#"*40, end="\n\n")
################################

print("Frozenset PART-3")
print("union, intersection, difference methods")
print("-"*20)
# --------------

sb_acc_customers = frozenset(["cust-1", "cust-2", "cust-3", "cust-4"])
loan_acc_customers = frozenset(["cust-3", "cust-4", "cust-5", "cust-6"])
print("sb_acc_customers:", sb_acc_customers)
print("loan_acc_customers:", loan_acc_customers, end="\n\n")

all_customers = sb_acc_customers.union(loan_acc_customers)
print("all_customers:", all_customers)

customers_not_having_loan = sb_acc_customers.difference(loan_acc_customers)
print("customers_not_having_loan:", customers_not_having_loan)

customers_having_both = sb_acc_customers.intersection(loan_acc_customers)
print("customers_having_both:", customers_having_both)

print("#"*40, end="\n\n")
################################
