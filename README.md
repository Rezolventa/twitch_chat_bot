# Twitch IO Chat Bot
A simple Twitch chat bot for handling media play and viewers activity.
# Getting started
Follow these simple instructions to get a copy of a project for personal use and testing.
## Prerequisites
To launch bot you have your MongoDB to be installed.

Also you will need a second twitch account for bot usage.
## Installing
Clone the repository, create a new virtual environment and install all dependencies from a requirements.txt file.
```
pip install -r requirements.txt
```
Link your MongoDB collection in mongo.py
```
collection = client.your_base.your_collection
```
Copy ```settings-example.py``` to ```settings.py``` and fill in your twitch accounts data such as your main account
name, bot account name and bot oath token.

***Warning: Never upload your twitch accounts data to public resources!*** 

Start bot with main.py. No parameters required.
```
python main.py
```
# Structure
```
/main.py
```
contains mostly commands and events
```
/mongo.py
```
got all the methods to work with database
```
/lexicon.py
```
adds some russian language declination features to bot answers
```
/sound/
```
has all the media files
# Xp and Currency system
Every time a viewer posts a message in chat the script counts how much time has passed since the previous message. If it's more than a minute the viewer gets and xp and a coin. This prevents spammers to get more points.

Basically, an xp amount shows how active the current viewer was through over the channel history while coins are kind of currency the viewer can spend.
## What do viewers spend currency on?
A viewer can trigger a specific audio meme with bot commands so the sound will be played on live-stream right away.
In addition a viewer can call commands to display his total xp and a number of currency in his pocket.
## Audio commands
Commands to play specific audio meme.
```
!clap
!shame
!tank
```
## Text commands
```
!help
```
a short tip for new viewers
```
!level
```
displays your level
```
!click
```
displays how many clicks were there during the stream
# TODO
The most wanted feature right now is to display viewer data online on live-stream as a dynamic html.
