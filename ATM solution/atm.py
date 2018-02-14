def atm(request,money):
	reminder = money - request
	allowed_papers = [100, 50, 10, 5, 1]

	if request <= 0:
		print "Must be more than 0 ,TRY more!"
	elif request > money:
		print "Sorry, There is no enough money,TRY less!"
		print "Your Account value is " + str(money)
	else :
		print "Requested:",request
		print "Your Balance is:" , reminder
		
		for x in allowed_papers:
			while request >= x:
				print "Give:", x
				request -= x


atm(277,500)
atm(1000,750)
atm(500,232)
atm(-500,1000)

######################################
