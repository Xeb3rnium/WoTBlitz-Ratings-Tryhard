# WoTBlitz Ratings Tool
Tired of being clapped by battle spamming sweats? Need to stalk the sleep schedules of unicums? Then this Ratings tool is for you!

Small cli python script for monitoring Ratings activity and threat modelling certain players on the leaderboard, inspired by <a href="https://github.com/x0rz/tweets_analyzer">x0rz's Tweet Analyzer</a> and some other shit while I was off my gob
<br><br><br>
![Rolling's Analysis](https://media.discordapp.net/attachments/307258554581254144/783890501576949760/lmao.png)
Thanks to Jylpah, Topdawg and RollingSwarm for useful input
<br><br>

# FUCK YOU TO WHOEVER DID THIS
![Go Fuck Yourself](https://media.discordapp.net/attachments/307258554581254144/784519086259306506/Screenshot_20201204-1828112.png)



# TEMPORARY NOTE 
Script will break if run outside season times, -u and -p needs finishing. Default also broken right now since not enough on Diamond leaderboard.
<br>
Works only for EU server but you can change the regions in the urls to na, ru or asia. Leagues can be changed to by changing 0 to 1, 2, 3 or 4


## How to use


### Install dependencies
```shell
pip install -r requirements.txt
```

### Usage
```shell
$ ./tryhardblitz.py
```
Will fetch the leaderboard and pull the top 30 players of Diamond league by default

### Help
```shell
$ ./tryhardblitz.py -h
WoTblitz Tryhard Ratings Tool v1.0
Written by ExtraBacon with help from Jylpah, Topdawg and RollingSwarm.

Usage: tryhardblitz [-h | --help] [-c <count>] [-u <username>] [-p <players>...]

Prints out a list of Blitz players and their ratings with colour coded latest battles by default, individual or lists of users can be passed too

Optional Arguments:
    -h, --help          Prints usage help
    -c COUNT            Print custom top players count
    -u USER             Check a player's rating and status
    -p PLAYERS          Check list of given players ratings and statuses

Colour Codes:
    Active a minute ago or less
    Active less than a battle ago
    Online within the last 3hours
    Online within the last 6hours
    Offline within half a day
    Offline for most of the day
    Offline for over a day

```

## Platforms
 * OSX/Unix
 * Windows (works on Powershell but breaks colours, better to use WSL)
 * Linux

## Python Compatibility
 * 3.x (recommended)

## TODO
 + Finish <-u> and <-p> parameters
 + Refactor and clean up retarded lines
 + User selected region input for multiple leaderboards
 + Implement graphs and logged activity for better threat intelligence
 + howtoargparse.png


<br><br><br>
oh yeah btw congrats to SPED for getting vibe checked by dual T57 Heavys and getting clapped 9-2 to RGN gg
![GET REKT RAIK](https://media.discordapp.net/attachments/307258554581254144/783890466960572426/moe.gif)
