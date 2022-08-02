import requests
import lxml
import json
import sqlite3
from bs4 import BeautifulSoup as bfs


def main():
	db = database('XIV.db')
	db.insert_action('GNB', 'Gnashing Fang', 'Weaponskill', 'Instant', '2.5s', 'Gnashing Fang go!!!')
	db.insert_action('GNB', 'Gnashing Fang', 'Weaponskill', 'Instant', '2.5s', 'Gnashing Fang go!!!')
	db.insert_action('PLD', 'Goring blade', 'Weaponskill', 'Instant', '2.5s', 'Goring blade go!!!')
	db.show_actions()
	db.close()



class database:
	def __init__(self, name):
		self.connection = sqlite3.connect(name)
		self.c = self.connection.cursor()

		with self.connection:
			self.c.execute("""CREATE TABLE IF NOT EXISTS Actions(
				Job text,
				Name text,
				Type text,
				Cast text,
				Recast text,
				Effect text
				)""")

			self.c.execute("""CREATE TABLE IF NOT EXISTS GearURLs(
				'URL' text
				)""")

	def close(self):
		self.connection.close()


	def show_actions(self):
		self.c.execute("SELECT * FROM Actions")
		print("Job")
		for line in self.c.fetchall():
			print(line)


	def insert_action(self, Job, Name, Type, Cast, Recast, Effect):
		with self.connection:

			#Check if already exists to insert/update
			self.c.execute("SELECT * FROM Actions WHERE Name = :Name", {'Name': Name})
				
			if len(self.c.fetchall()) == 0:
				self.c.execute("INSERT INTO Actions VALUES (:Job, :Name, :Type, :Cast, :Recast, :Effect)",
					{'Job':Job, 'Name':Name, 'Type':Type, 'Cast':Cast, 'Recast':Recast, 'Effect':Effect})
			else:
				self.c.execute("""UPDATE Actions SET
					Job = :Job, 
					Name = :Name, 
					Type = :Type, 
					Cast = :Cast, 
					Recast = :Recast, 
					Effect = :Effect
					WHERE Job = :Job AND Name = :Name""",
					{'Job':Job, 'Name':Name, 'Type':Type, 'Cast':Cast, 'Recast':Recast, 'Effect':Effect})





if __name__ == "__main__":
	main()