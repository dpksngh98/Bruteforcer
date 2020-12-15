import requests
import urllib
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.error import HTTPError
import urllib.request
import urllib3
http = urllib3.PoolManager()


def is_url(new_url):
	# try:
	# 	r = req.head(new_url)
	# 	print(new_url," ",r.status_code)
	# except requests.ConnectionError:
	# 	print("failed to connect")

	# Checking the status codes by passing the request
	# Status codes are validated online
	try:
		connection = urllib.request.urlopen(new_url)
		return connection.getcode()          # When there is success code found
		connection.close()
	except HTTPError as e:
		return e.getcode()					# When URL is not valid and codes like 404,403 etc are found
	
def main():

	status_code_list=[]   # To store n number of success codes
	url_result_list=[]    # To store the valid webapp URL's

	#taking url as input from user
	url=input("Enter a URL in format (https://.../) :")

	num = int(input("Enter the number of successful status code you want to enter :"))

	# storing n success codes in the list
	for i in range(0,num):
		status_code_list.append(int(input("Enter next no :")))

	#parsing the file
	with open('wordlist1.txt','r') as file: 
   
   	    # reading each webpath from file     
		for word in file:

			#New url is formed ("url/word")
			new_url=url+word		

			 #function to check the status of every url
			status = is_url(new_url)
			for i in status_code_list:
				if status == i:							# Checking if returned code matches with success codes present in the list
					url_result_list.append(new_url)		# When condition is true add URL to the list
	
	# Printing the list
	for i in url_result_list:
		print(i)

if __name__ == '__main__':
	main()
