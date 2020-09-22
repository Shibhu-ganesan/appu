# 1) returns all the objects in a model
customer = Customer.objects.all()
# 2) returns the first customer
Customer.objects.first()
# 3) returns last
Customer.objects.last()
# 4) return customer by name
customer_byname = Customer.objects.get(name="Thirunavukarasu")
# can get the id of the specific customer
customer_byname.id
# and other attributes as well
customer_byname.email
# what if guys with same name exists
customer_byid = Customer.objects.get(id=4)
# filtering according to a category
products = Product.objects.filter(category="Out door").count()  # this returns the count
# we can also add as many attributes as we want as long as they are part of a model
# Ordering ascending
products = Product.objects.all().order_by('id')
# descending
products = Product.objects.all().order_by('-id')
# Many to many query
products = Product.objects.filter()
# to get the orders placed by the customer
cust = Customer.objects.first()
cust.order_set.all()
