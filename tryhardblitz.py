#!/usr/bin/env python3
#
# WoTBlitz Ratings threat intelligence tool for sweats like you and me! Ping me on Discord for any questions @ExtraBacon
#
#TODO: User input str region
import sys, requests, datetime, time, progress.bar

APP_ID = "a125d0975020cd5d594f5b940fdaae60"
HEADER = {"Accept-Encoding": "WoTBlitz Tryhard"}
API = "https://api.wotblitz.eu/wotb/account/"
RATINGS = "https://eu.wotblitz.com/en/api/rating-leaderboards/"


class realms:
	na = 'com'
	eu = 'eu'
	cis = 'ru'
	asia = 'asia'

class colors:
	red = '\033[91m'
	orange = '\033[9m' # Not working on OSX? Need to fix
	yellow = '\033[93m'
	green = '\033[92m'	
	cyan = '\033[96m'
	blue = '\033[94m'
	magenta = '\033[95m'
	grey = '\033[90m'
	default = '\033[0m'
	blink = '\033[5m'
	inverse = '\033[7m'
	bold = '\033[1m'


curl = lambda url: requests.get(url, headers=HEADER, allow_redirects=True)

leaderboard = lambda: curl(RATINGS + "league/0/top/").json()['result'] if curl(RATINGS + "league/0/top").status_code == requests.codes.ok else exit("Error in fetching leaderboard")

userid = lambda nick: str(curl(API + "list/?application_id=%s&search=%s" % (APP_ID, nick)).json()['data'][0]['account_id']) if curl(API + "list/?application_id=%s&search=%s" % (APP_ID, nick)).json()['status'] == "ok" else exit("Error in fetching user ID") # Oh my god this is so retarded Wargaming whyyyyyy put the error status INSIDE the response instead of BEING the response for fuck sake

lastbattle = lambda uid, nick: curl(API + "info/?application_id=%s&account_id=%s" % (APP_ID, uid)).json()['data'][str(uid)]['last_battle_time'] if curl(API + "info/?application_id=%s&account_id=%s" % (APP_ID, uid)).json()['status'] == "ok" else exit("Error in fetching last battle timestamp")

#ego = lambda test: curl(API + "info/?application_id=%s&account_id=%s" % (APP_ID, uid)).json()['data']



def main(): # Yes I know I should be using argparse stfu
	try:
		if len(sys.argv) == 1:
			init(30)
		elif(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
			help()
		elif sys.argv[1] == "-c" and len(sys.argv) == 3 and isinstance(int(sys.argv[2]), int):
			init(int(sys.argv[2]))
		elif sys.argv[1] == "-u" and len(sys.argv) == 3 and isinstance(sys.argv[2], str):
			init(1, names=[str(sys.argv[2])])
		else:
			help()
	except:
		print(f"\n---------------{colors.cyan}Error Occured{colors.default}----------------\n")

def init(rank, names=[]):
	print(f"\n-----{colors.cyan}WoTBlitz Tryhard Ratings Tool v1.0{colors.default}-----\n")
	fetch(rank, names)
	print(f"\n---------------{colors.cyan}Finished{colors.default}----------------\n")


def fetch(rank, names=[]):
	if names:
		with progress.bar.ChargingBar("Fetching Your League:", max=1) as bar:
			hitlist = [{'spa_id': userid(names), 'score': 0000, 'nickname': names[0], 'clan_tag': "AFK"}] # FIX THIS: STORE USERID TOO
			bar.next()
		bar.finish
		#battles = custom(rank, hitlist)
		battles = latest(rank, hitlist)




	else:
		with progress.bar.ChargingBar("Fetching Leaderboard:", max=1) as bar:
			try:
				hitlist = leaderboard() # Grab UIDS, usernames and clans
				bar.next()
			except ConnectionError:
				print("HTTP Request Error")
		bar.finish
		battles = latest(rank, hitlist)





	with progress.bar.ChargingBar("Loading Current Sweats:", max=1) as plebs: # Meme
		if len(battles) != rank:
			exit("Error in checking battle times")
		else:	
			plebs.next()
	plebs.finish

	for x in range(len(battles)): # TODO: User param ranges, spacer colour coding, cache/logging graphs
		if names:
			period = int(time.time()) - battles[0][userid(hitlist[0])] # FIX THIS: STORE USERID
		else:
			period = int(time.time()) - battles[x][hitlist[x]['spa_id']]
		unit = "secs"
		if period <= 10800: #TODO: Fine tune these thresholds, add user input var for this?
			if period <= 3600:
				if period <= 360:
					if period <= 60:
						status = colors.green + colors.inverse
						period = colors.blink + str(period) + colors.bold
					else:
						status = colors.green + colors.bold
						period = str(int(period/60)) + colors.bold
						unit = "mins"
				else:
					status = colors.green + colors.bold
					period = str(int(period/60)) + colors.bold
					unit = "mins"
			else:
				status = colors.green
				period = str(int((period/60)/60))
				unit = "hrs"
		elif period <= 21600: # Within 6hrs
			status = colors.yellow
			period = str(int((period/60)/60))
			unit = "hrs"
		elif period <= 43200: # Within 12hrs
			status = colors.red
			period = str(int((period/60)/60))
			unit = "hrs"
		elif period > 86400: # Over a day
			status = colors.default
			period = str(int(((period/60)/60)/24))
			unit = "days"
		else: # Over 12hrs but less than a day
			status = colors.grey
			period = str(int((period/60)/60))
			unit = "hrs"

		output(x, hitlist, battles, period, unit, status)







def latest(rank, hitlist):
	with progress.bar.ChargingBar("Fetching Latest Battles:", max=30) as bar:
		latest = []
		try:
			for i in range(rank):
				posix = {hitlist[i]['spa_id']: lastbattle(hitlist[i]['spa_id'], hitlist[i]['nickname'])} # Is there an API call that takes in an array of UIDs instead of calling this 30 times?
				latest.append(posix)
				bar.next()
		except ConnectionError:
			print("HTTP Request Error")
	bar.finish()
	return latest

"""
def custom(rank, hitlist):
	with progress.bar.ChargingBar("Fetching Player Battles:", max=30) as bar:
		latest = []
		try:
			for i in range(rank):
				posix = {userid(hitlist[0]): lastbattle(userid(hitlist[0]), hitlist[0])}
				latest.append(posix)
				bar.next()
		except ConnectionError:
			print("HTTP Request Error")
	bar.finish()
	return latest
"""








def output(x, hitlist, latest, period, unit, status):
	print("\n%s===============================================%s" % (colors.blue, colors.default))
#	print(f"      {hitlist[x]['nickname']}", "%s[%s] %s-%s" % (colors.grey, hitlist[x]['clan_tag'], colors.default, colors.magenta), hitlist[x]['score'], colors.default) # Nightmare to align for fuck sake
	print("         %s%s%s -" % (colors.magenta, hitlist[x]['score'], colors.default), hitlist[x]['nickname'] + "%s[%s]%s" % (colors.grey, hitlist[x]['clan_tag'], colors.default)) # Points first in same column
	print("    %s%s%s" % (status, time.strftime("%A %d %B %Y %I:%M:%S%p %Z", time.localtime(latest[x][hitlist[x]['spa_id']])), colors.default)) # Last battle time
	print("\t        ", f"{colors.grey}{period}{unit}{colors.default} ago")
	print("%s===============================================%s\n" % (colors.blue, colors.default))



def help():
	print("WoTblitz Tryhard Ratings Tool v1.0\nWritten by ExtraBacon with help from Jylpah, Topdawg and RollingSwarm.\n")
	print("Usage: tryhardblitz [-h | --help] [-c <count>] [-u <username>] [-p <players>...]\n")
	print("Prints out a list of Blitz players and their ratings with colour coded latest battles by default, individual or lists of users can be passed too\n")
	print("Optional Arguments:")
	print("    -h, --help          Prints usage help")
	print("    -c COUNT            Print custom top players count")
	print("    -u USER             Check a player's rating and status")
	print("    -p PLAYERS          Check list of given players ratings and statuses\n")
	print("Colour Codes:")
	print(f"    {colors.green + colors.inverse}Active a minute ago or less{colors.default}")
	print(f"    {colors.green + colors.bold}Active less than a battle ago{colors.default}")
	print(f"    {colors.green}Online within the last 3hours{colors.default}")
	print(f"    {colors.yellow}Online within the last 6hours{colors.default}")
	print(f"    {colors.red}Offline within half a day{colors.default}")
	print(f"    {colors.grey}Offline for most of the day{colors.default}")
	print(f"    Offline for over a day\n")


if __name__ == "__main__":
    main()
