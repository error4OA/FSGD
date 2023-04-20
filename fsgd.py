#free steam game downloader by cragdor the destroyer
import requests
import random
import os
print("Welcome to FSGD 1.0, the open-source game downloader")
while True:
	print("What do you want to download?\n\n1. Pizza Tower\n2. Wobbly Life\n")
	answer = int(input("?. "))

	if answer == 1:
		print("Downloading, this will take a while...")
		game = "https://download193.uploadhaven.com/1/application/zip/Y3hxSZVE5ZjlrZd4etRpd8AjDdkEw8S4VZxv8Xbp.zip?key=H_vyTKYaMvOsy7-DnD_Qyg&expire=1682023400&filename=Pizza.Tower.v1.0.311.zip"
		request = requests.get(game, stream=True)
		with open(str(random.randint(1, 1000001)) + ".zip", "wb") as downloading:
			for chunk in request.iter_content(chunk_size=3072):
				downloading.write(chunk)
		print("Done!")
	elif answer == 2:
		print("Downloading, this will take a while...")
		game = "https://download131.uploadhaven.com/1/application/zip/ywgQHYXM02dp415tjnfTDVxRkpHCLuShtGXJPsRi.zip?key=0UhnVMhgqf9hnCI5xjLy6Q&expire=1682107998&filename=Wobbly.Life.v0.8.1.zip"
		request = requests.get(game, stream=True)
		with open(str(random.randint(1, 1000001)) + ".zip", "wb") as downloading:
			for chunk in request.iter_content(chunk_size=3072):
				downloading.write(chunk)
		print("Done!")

