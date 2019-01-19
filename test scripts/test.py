import wikipedia
import MySQLdb

query = "UFO Sightings"

search =  wikipedia.search(query, results=10, suggestion=False)

#section = wikipedia.WikipediaPage('UFO sightings in outer space').section('Incidents')
section = wikipedia.WikipediaPage('UFO sightings in outer space')

#declare database
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     password="",  # your password
                     db="alien",
					 charset='utf8')

arr = []
for item in search:
    links = wikipedia.WikipediaPage(item).links
    arr = list(set().union(arr,links))
print(arr)
