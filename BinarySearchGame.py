# WorkFlow: You Choose A Number In Any Range You Determine In Your Mind, Then Script Guess Your Number Based On BinarySearch Algorithm

# Get Low And High Limits
def limits():
	pas = 'no'
	while pas != 'yes':
		try:
			lh = input('\nChoose Your Number In Your Mind And Enter Low And High Numbers(x - y): ').strip().split('-')
			l = int(lh[0])
			h = int(lh[1])
			if h>l:
				pas = 'yes'
				return l, h
			elif l>h:
				pas = 'yes'
				return h, l
			else:
				pass
		except:
			print('Enter Limits In Right Format! (x - y)\n')
			pass

# Evaluate Guess
def ask(guess):
	pas = 'no'
	while pas != 'yes':
		res = input(f'Is {guess} Correct? (y=yes, l=too low, h=too high)')
		if res=='y' or res=='l' or res=='h':
			pas = 'yes'
			return res
		else:
			print('Invalid Answer!')
			pass

# Calculate Guess Based On BinarySearch Algorithm
def calculate():
	# Count Attempts
	attempts = 0
	l, h = limits()
	pas = 'n'
	while pas != 'y':
		if l==h:
			print('\nSomeThings Wrong Here!!!!\nTry Again And Remember Your Number!!!!')
			break
		# Main Logic
		if h-l<=1 and res=='l':
			guess = l + 1
		elif h-l<=1 and res=='h':
			guess = l
		else:
			guess = int((h-l)/2 + l)
		res = ask(guess)
		if res=='y':
			print(f'\n{50*"*"}\nI Guessed Your Number In {str(attempts)} attempts')
			pas = 'y'
		elif res=='l':
			attempts += 1
			l = guess
		elif res=='h':
			attempts += 1
			h = guess

# Run
calculate()

# *********** Telegram: @eweraohw ***********
