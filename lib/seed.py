from models import Base, Company, Dev, Freebie
from debug import session


session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()


company1 = Company(name="TechCorp", founding_year=2001)
company2 = Company(name="DevWorks", founding_year=1999)


dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

session.add_all([company1, company2, dev1, dev2])
session.commit()


freebie1 = company1.give_freebie(dev1, "T-Shirt", 25)
freebie2 = company1.give_freebie(dev2, "Sticker Pack", 5)
freebie3 = company2.give_freebie(dev1, "Coffee Mug", 15)


session.add_all([freebie1, freebie2, freebie3])
session.commit()

print("Seed data created!")
