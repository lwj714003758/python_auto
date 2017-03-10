#!/usr/bin/python
import sys
slary = int(raw_input("input your slary:"))
products = ['car','iphone','Mac','coffee','tea']
prices = [200000,4799,10000,35,20]
shop_list = []
while True:
	print "Welcome,things you can buy as below:"
	for p in products:
		product_index = products.index(p)
		price = prices[product_index]
        	print p,'\t', price 
	choice = raw_input("pls choose a shop to buy!\n")
	f_choice = choice.strip()
	if f_choice in products:
		print '\33[36;1mYes,%s is in the list\33[0m' % f_choice
	else:
		print  '\33[36;1mNo,%s is not in the list\33[0m' % f_choice
	if slary > prices[products.index(f_choice)]:
        	shop_list.append(f_choice)
		print "%s added to shoplist!" % f_choice
       		slary = slary - prices[products.index(f_choice)]
        	print "now,your money left %d" % slary
       		#go_on = raw_input("do you want to go on shopping? yes/no\n")
       		#if go_on == 'yes ':
			#continue	
		#else:exit 
	else:
		if slary  <  min(prices):
			print "sorry,rest of your slary cannot buy anything! 88\n"
                	print "you have bought these thing: %s" % shop_list
			sys.exit()
		else:
			print "sorry,you cannot afford this product,please try other one!\n"

         
       
