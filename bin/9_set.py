"""
set:
        -- To keep multiple values like list of employee names
        -- We can keep unique values
        -- index number will not be there for each value
"""
print("set PART-1")
print("Store values")
print("-"*20)
# --------------

my_set = {10, 10, 10, "python", "python", "java", "java"}
print(my_set)
# OR
my_set = set([10, 10, 10, "python", "python", "java", "java"])
print(my_set)

# If we want index then convert to other type like list/tuple etc
# L = tuple(my_set)
# OR we can use any loops to iterate

print("#"*40, end="\n\n")
################################

print("set PART-2")
print("Methods present inside 'set' class")
print("-"*20)
# --------------

print(dir(set))

print("#"*40, end="\n\n")
################################

print("set PART-3")
print("union, intersection, difference methods")
print("-"*20)
# --------------

sb_acc_customers = set(["cust-1", "cust-2", "cust-3", "cust-4"])
loan_acc_customers = set(["cust-3", "cust-4", "cust-5", "cust-6"])
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

print("set PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# --------------

sb_acc_customers = set(["cust-1", "cust-2", "cust-3", "cust-4"])
loan_acc_customers = set(["cust-3", "cust-4", "cust-5", "cust-6"])
print("sb_acc_customers:", sb_acc_customers)
print("loan_acc_customers:", loan_acc_customers, end="\n\n")

# ADD
sb_acc_customers.add("cust-5")
print("sb_acc_customers after adding cust-5:", sb_acc_customers)

# REMOVE
sb_acc_customers.remove("cust-1")
print("sb_acc_customers after removing cust-1:", sb_acc_customers)

# UPDATE
# Replace cust-3 with cust-30
sb_acc_customers.remove("cust-3")
sb_acc_customers.add("cust-30")
print("sb_acc_customers after changing cust-3 to 30:", sb_acc_customers)

# UPDATE
all_customers = sb_acc_customers.union(loan_acc_customers)
sb_acc_customers.update(loan_acc_customers)
print("all_customers:", all_customers)
print("sb_acc_customers after updating loan_acc_customers:", sb_acc_customers)

print("#"*40, end="\n\n")
################################
