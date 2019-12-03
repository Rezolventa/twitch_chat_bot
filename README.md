# Twitch IO Chat-bot
A simple Twitch chat bot for handling media play and viewers activity.
# How to install
To launch bot you have your MongoDB to be installed. Clone the repository, crate a new virtual env and install all dependencies from a requirements.txt file.
```
pip install -r requirements.txt
```
Link your MongoDB collection in mongo.py
```
collection = client.your_base.your_collection
```
Start bot with main.py. No parameters required.
```
python main.py
```
# Structure
main.py contains mostly commands and events

mongo.py got all the methods to work with database

lexicon.py adds some russian language features to bot answers

sound/ has all the media files
# Xp and Coins system
Everytime a viewer posts a message in chat the script counts how much time has passed since the previous message. If it's more than a minute the viewer gets and xp and a coin. This prevents spammers to get more points.

Basically, an xp amount shows how active the current viewer was through over the channel history while coins are kind of currency the viewer can spend.
# What do viewers spend currency on?
A viewer can trigger a specific '.wav' sound with commands so the sound will be played on live-stream right away.
In addition a viewer can call commands to display his total xp and a number of coins in his pocket.
# TODO
The most wanted feature right now is to display viewer data online on live-stream as a dynamic html.
