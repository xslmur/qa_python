from pony.orm import Database

db = Database()
db.bind(provider='postgres', user='test', password='test', host='localhost', database='pets')

