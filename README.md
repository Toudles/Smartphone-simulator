You've been hired by a large telecommunications company to write a program to help people add and remove apps from their smartphone. To do this you should write a CLASS that models a smartphone. Your class should do the following:

class Smartphone:

	# construct a new Smartphone
	# smartphones need to keep track of how much space they have left (integer)
	# they also need to keep track of their name (string)
	# smartphones will need some kind of internal system to keep track of all of 
	# the apps that are installed, along with their size.  a list or a dictionary
	# would be useful here.
	# when a phone is constructed the 'report' method should be called (see below)
	# this method returns nothing and simply prints the desired output to the user
	def __init__(self, capacity, name):

	# add a new app to the smartphone given an appname (string) and an appsize (integer)
	# if the app is already installed, reject it.  if the phone cannot hold any additional
	# apps because the capacity has been reached, reject it.
	# this method returns nothing and simply prints the desired output to the user
	def add_app(self, appname, appsize):

	# removes an app from the phone based on appname (string)
	# if the app is not installed, reject it
	# this method returns nothing and simply prints the desired output to the user
	def remove_app(self, appname):

	# checks to see if an app is installed based on appname (string)
	# returns True if the app is installed, False if it is not
	def has_app(self, appname):

	# returns the current space available on the phone (integer)
	def get_available_space(self):

	# prints a detailed report that describes the following:
	# Name of phone
	# Capacity of phone
	# Available space
	# # of apps installed
	# a listing of all apps installed, in alphabetical order, with their sizes
	# this method returns nothing and simply prints the desired output to the user
	def report(self):
