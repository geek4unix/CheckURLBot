# CheckURLBot

A discord bot (POC) to check messages and react to them , in this poc we translate the hostname to an ip address and check that in a list of known bad networks. 

If the Server/Link IP matches a known bad network, we display some reactions and the bot sends a message. If the URL does not appear in the 'bad list' , the bot does nothing

There is very little error checking, this is just a POC.

Getting setup  ...
------------------

Python3 - version 3.9 and up required

Use pip to do a local install of discord.py 

```pip install -U discord.py```

Get the latest version of the file: https://iplists.firehol.org/files/firehol_level1.netset

Remove comment lines

Setup Bot on discord.com
------------------------

Register the bot on discord dev site, link to a channel

Developer website: https://discord.com/developers/applications/

export an environmental variable with your bot access token:

```export CHECKURLBOT_TOKEN=1234...78910```

How to use it ...
-----------------


```
(bot-env) user@mbp CheckURLBot % python3 checkurlbot.py
Loading rules
Loaded 2497 entries
We have logged in as CheckURLBot#8384
<re.Match object; span=(0, 7), match='http://'> http://neilstest.org/ neilstest.org 131.143.1.1
```

This is what it looks like when a hostname's resolved IP address is in the 'bad list':

<img width="450" alt="Screenshot 2022-04-16 at 17 38 02" src="https://user-images.githubusercontent.com/6726149/163684267-863c7542-e906-4a1c-8466-b0cd119a52f5.png">

