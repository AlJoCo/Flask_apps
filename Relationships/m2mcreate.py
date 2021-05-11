from m2mapp import db, Products_ordered, Customers, Baskets

db.create_all() # Creates all table classes defined

j = Customers(name = 'Johnny')
c = Customers(name = 'Craig')
m = Customers(name = 'Molly')
db.session.add(j)
db.session.add(c)
db.session.add(m)
db.session.commit()

x = Products_ordered(name='Hamburger', quantity = 3)
y = Products_ordered(name='Lolipop', quantity = 4)

db.session.add(x)
db.session.add(y)
db.session.commit()