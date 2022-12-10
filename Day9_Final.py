import Day9_art

#variables 
end_of_bidding = False
bidding = {}

def calculate_bid(bids):
    highest_bid = 0
    for key in bids:
        if bids[key] >  highest_bid:
            highest_bid = bids[key]
            name = key
            
    print('The winner is ' + name + ' with a bid of $' + str(highest_bid))
    print(Day9_art.logo)

print('Welcome to the secret auction program.')
while not end_of_bidding: 
	name = input('What is your name?: ')
	bidding[name] = int(input('What is your bid? $'))

	done = input('''Are there any other bidders? Type 'yes' or 'no'. \n''').lower()

	if done == 'yes': 
		end_of_bidding = False
	else: 
		end_of_bidding = True

calculate_bid(bidding)