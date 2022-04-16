import discord,re,socket,ipaddress,time,os
from urllib.parse import urlparse

# Check for environmental variable for bot token
try:
    CHECKURLBOT_TOKEN = os.environ.get('CHECKURLBOT_TOKEN')
except:
    print("Could not find ennvironment variable: CHECKURLBOT_TOKEN, exiting ...")
    exit(1)

cross="❌"
fire="🔥"

with open("firehol_level1.netset") as file:
    print("Loading rules")
    lines = [line.rstrip() for line in file]
    #print(lines)
    entries=len(lines)
    print("Loaded "+str(entries)+" entries")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    find_regex="(http|https)\:\/\/"
    regex = re.compile(find_regex)
    result = regex.search(message.content)

    if result:
        parsed_url=urlparse(message.content)
        hn=parsed_url.netloc
        client_ip=socket.gethostbyname(hn)
        print(result,message.content,hn,client_ip)
        # check if IP address matches any 'bad' ranges.
        addr4 = ipaddress.ip_address(client_ip)
        for line in lines:
            if addr4 in ipaddress.ip_network(line):
                public_post="Suspect IP range ! %s - %s" % (hn,client_ip)
                await message.add_reaction(cross)
                await message.add_reaction(fire)
                await message.channel.send(public_post)
        else:
            time.sleep(0.000001)
            
    else:
        print("No Match.")

client.run(CHECKURLBOT_TOKEN)
