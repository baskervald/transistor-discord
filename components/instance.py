class ServerInstance:
    def __init__(self, client, server):
        self.server_obj = server
        self.client = client
        self.member = self.server_obj.me
        self.text_channel_instances = []

    def register_channel(self, channel):
        self.text_channel_instances[channel.id] = ChannelInstance(self.client, self, channel)

    def deregister_channel(self, channel):
        self.text_channel_instances.pop(channel.id)


class ChannelInstance:
    def __init__(self, client, server_instance, channel):
        self.parent = server_instance
        self.channel_obj = channel
        self.client = client
        self.permissions = self.channel_obj.permissions_for(client.user)

