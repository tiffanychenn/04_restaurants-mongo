import pymongo

connection = pymongo.MongoClient("homer.stuy.edu")

db = connection.test
collection = db.restaurants

boroughs = collection.find({"borough":"Brooklyn"})

print "All restaurants in a specified borough (Brooklyn)"

print "\n\n\n"

for i in boroughs:
	print i

print "\n\n\n"

zipcodes = collection.find({"address.zipcode":"11211"})

print "All restaurants in a specified zipcode (11211)"

print "\n\n\n"

for i in zipcodes:
	print i

print "\n\n\n"

grades = collection.find({"address.zipcode":"11211", "grades.grade": "A"})

print "All restaurants in a specified zipcode (11211) and a specified grade (A)"

print "\n\n\n"

for i in grades:
	print i

print "\n\n\n"

scores = collection.find({"address.zipcode":"11211", "grades.score": {"$lt":12}})

print "All restaurants in a specified zipcode (11211) and a score of less than 12"

print "\n\n\n"

for i in scores:
	print i

print "\n\n\n"

names = collection.find({"borough": "Manhattan", "$or": [{"cuisine": "Caribbean"}, {"cuisine": "Korean"}]})

print "All restaurants in a specified borough (Manhattan) and serving either Caribbean or Korean cuisine"

print "\n\n\n"

for i in names:
	print i