""" This file is consist of user credentials. """

class User:
	""" Base class of User. """

	UNAME = 'your_username'
	PASSWD = 'your_password'

class Email:
	""" Class inherited from User base class, and store email credentials to notify user on product 
	availablity."""

	EMAIL = 'your_email'
	EMAILPASSWD = 'your_email_password'
	RECEIVER = ['email_of_receiver']
	SUBJECT = 'subject of email'
	BODY = 'body of email'
