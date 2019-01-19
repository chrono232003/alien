import wikipedia
import MySQLdb

query = "UFO Sightings"

search =  wikipedia.search(query, results=30, suggestion=False)

list = ['No. 604 Squadron RAF', 'Monmouth County', 'Dyatlov Pass incident', "The Trindade Island's UFO", 'Stonehenge incident', 'Unidentified flying objects', 'Roswell, New Mexico', 'UFO sightings in Mexico', '1974 Abduction Event', 'Petrozavodsk phenomenon', 'Kelly Cahill Abduction', 'Wales UFO sightings', 'Barney and Betty Hill', 'Milton Torres 1957 UFO Encounter', 'Douglas DC-4', 'Ellsworth UFO sighting', 'UFO sightings in Iran', 'Narrative of the abduction phenomenon', 'History of alien abduction claims', 'Point Pleasant, West Virginia', 'Nash-Fortenberry UFO sighting', 'UFO sightings in outer space','Falcon Lake incident', 'The Hague UFO sighting', 'Advanced Aviation Threat Identification Program', 'Ural Mountains', 'Old-Saybrook UFO incident', 'Betty and Barney Hill abduction', 'Rendlesham Forest incident', '2009 Norwegian spiral anomaly', 'UFO sightings in Brazil', 'Voronezh UFO incident', 'Chiles-Whitted UFO Encounter', 'Tananarive UFO incident', 'Mass UFO sighting', 'UFOlogy', 'Center for UFO Studies', 'Lockheed EC-121 Warning Star', 'D.C. UFO incident', 'Project Magnet', 'Robert C. Seamans, Jr.', 'Gemini 4', '2018 California UFO sighting', 'Vashon Island incident', 'America West Airlines Flight 564', 'Manbhum UFO sighting', 'Michigan Swamp Gas Sightings', 'Mariana UFO incident',  'Titograd UFO incidents', 'Pascagoula Abduction', 'Men in Black', 'UFO sightings in the Canary Islands', 'Grey alien', 'List of prizes for evidence of the paranormal', 'Mystery airship', 'Space jellyfish', 'Catalina Island UFO', 'Little Rissington UFO incident', 'Alien abduction', 'Interdimensional hypothesis', 'UFO sightings in Canada', 'Identification studies of UFOs', '2011 Vancouver UFO sighting', 'Reptilian humanoid',  'Electronic voice phenomenon', 'Hangzou UFO sighting', 'Apollo 11', 'The Flying Saucers Are Real', 'Ufology Research of Manitoba', 'List of reported UFO sightings', 'UFO sightings in Norway', 'Mutual UFO Network', 'Japan Air Lines flight 1628 incident', 'The Tinley Park Lights', 'The Judy Doraty Abduction', 'Erasmuskloof Sighting', '1976 Tehran UFO incident', 'Valensole UFO incident', 'UFOs in fiction', 'List of investigations of UFOs by governments', 'Oldenburg UFO Encounter', 'Travis Walton UFO incident', 'Lakenheath-Bentwaters incident', 'USS Nimitz UFO incident', 'Project Grudge', 'Mantell UFO incident', 'Aquatic ape hypothesis', 'Ed White (astronaut)', '2015 Gorakhpur UFO sighting', 'Flying Saucer Working Party', 'Graaff-Reinet sighting', 'Ubatuba UFO Explosion','Kecksburg UFO incident', 'Gulf of Mexico UFO Encounter', 'Shag Harbour UFO incident', 'Belgian UFO wave', 'Reported UFO sightings in the United Kingdom', 'Black triangle (UFO)', 'Varginha UFO incident', 'New Mexico, UFO incident', 'Warrenton Sighting', 'Kelly–Hopkinsville encounter', '1976 Canary Isles sightings', 'Prince Christian UFO sighting', 'Warden Sighting', 'UFO sightings in India', 'Exeter incident', 'Stephenville, Texas UFO sightings', 'Hudson Valley Sightings', 'UFO sightings in Australia', 'Portage County UFO Chase',  'UFO sightings in Italy', 'Arequipa UFO incident', "2006 O'Hare International Airport UFO sighting", 'Flying saucer', '1952 Washington D.C. UFO incident', 'McMinnville UFO photographs', 'List of unexplained explosion events', '2018 Arizona UFO sightings', 'Sasolburg Sighting', 'Coyame UFO incident', 'Chiles-Whitted UFO encounter', 'Skylab 3 UFO Encounter', 'Autumn 1954 European UFO wave', 'Southern Illinois UFO incident', 'Morristown UFO', 'Manises UFO incident', 'Outer space', 'List of UFO religions', 'Alien abduction entities', 'Colorado UFO sighting', '1965 Craft Landing',  'Berwyn Mountain UFO incident', 'Mantell UFO Incident', 'UFO sightings in South Africa', 'UFO sightings in Belarus', 'Little green men', 'Extraterrestrial life', 'Stanford Abduction', 'Sperry UFO case','Aurora, Texas, UFO incident', '2007 Kolkata UFO sighting', 'Indigo children', 'Kenneth Arnold UFO sighting', 'Prescott Sightings', 'Cape Girardeau UFO crash', 'Maury Island incident', 'Fukuoka Incident', '1972 UFO sightings in the eastern Cape', 'Baviaanspoort Sighting', 'Allagash abductions', 'Crop circle', 'Moon landing conspiracy theories', 'STS-80 incidents', 'UFO sightings in Thailand', '2014 Texas UFO sightings', '2018 Ireland UFO sighting', 'Carson Sink UFO incident', 'ufology and pseudoscience', 'UFO sightings in Russia', 'Westall UFO', 'Kensington PEI Sighting', 'UFO sightings in the United States', 'UFO sightings in the Philippines', 'Nazi UFOs', 'Harbour Mille incident', 'UFO-Memorial Ängelholm', 'Jimmy Carter UFO incident', 'Val Johnson incident', 'UFO sightings in Argentina', 'Levelland UFO case', 'Airplane Disc Sighting', '1979 Mindalore Incident', 'Roswell UFO incident', 'La Pampa Province sighting', 'Area 51', '2007 Alderney UFO sighting', 'UFO sightings in Indonesia', 'Emilcin Abduction', 'UFO convention', 'Gulf Breeze UFO incident', 'List of alleged extraterrestrial beings', 'Portage County UFO chase', 'UFO sightings in China', 'Alien abduction claimants', 'Middelburg Witbank Sighting', 'Booysens Sighting', 'Cisco Grove Encounter', 'Ancient astronauts','Close encounter of Cussac', 'Tierpoort Sighting', 'Majestic 12', 'Index of ufology articles', '1952 Salem, Massachusetts UFO incident', 'Westendorff UFO sighting', 'Delphos UFO Incident', 'UFO sightings in New Zealand', 'Ariel UFO incident', 'Clarenville UFO Sighting', 'Kaikoura lights', 'National Investigations Committee On Aerial Phenomena', 'The RB-47 UFO Encounter']

#declare database
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     password="",  # your password
                     db="alien",
					 charset='utf8')

#for item in search:
for item in list:
	try:
		#going nuts in this piece
		content = wikipedia.WikipediaPage(item).content
		content = content.replace("'", r"\'")
		item = item.replace("'", r"\'")

		images = wikipedia.WikipediaPage(item).images
		image = ""
		if images:
			image = images[0]
		# you must create a Cursor object. It will let
		#  you execute all the queries you need
		cur = db.cursor()

		# Use all the SQL you like
		sql = "INSERT INTO stories (title, article, image) VALUES('" + item + "', '" + content + "', '" + image + "')"
		#print(sql)
		cur.execute(sql)
	except:
		print("error with " + item)

db.commit()
db.close()
