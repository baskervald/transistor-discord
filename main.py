import discord
import asyncio

from components.instance import ServerInstance

client = discord.Client()

class Transistor:
    def __init__(self, client):
        self.client = client
        self.server_instances = {}

    def get_server_instance(self, id):
        return self.server_instances[id]

    def register_server(self, server):
        print("Created instance of ServerInstance for " + server.name + " (" + server.id + ")")
        self.server_instances[server.id] = ServerInstance(self.client, server)

    def deregister_server(self, server):
        print("Destroyed instance of ServerInstance for " + server.name + " (" + server.id + ")")
        self.server_instances.pop(server.id, None)

bot = Transistor(client)

@client.event
async def on_ready():
    print("----------------------")
    print("Logged in as " + client.user.name)
    print("Registering servers then channels, recursively")
    for server in client.servers:
        bot.register_server(server)
        inst = bot.get_server_instance(server.id)
        for channel in server.channels:
            inst.register_channel(channel)

    for key, value in server_instances:
        print(value.server_obj.name)
        for key, value in value.text_channel_instances:
            print(value.channel_obj.name)


@client.event
async def on_server_join(server):
    bot.register_server(server)

async def on_server_remove(server):
    bot.deregister_server(server)

async def on_channel_create(channel):
    if not channel.is_private:
        bot.get_server_instance(channel.server.id).register_channel(channel)

async def on_channel_delete(channel):
    if not channel.is_private:
        bot.get_server_instance(channel.server.id).deregister_channel(channel)


