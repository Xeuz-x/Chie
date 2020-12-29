#   Copyright 2020 Nhalrath
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import discord
from discord.ext import commands

class SayCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.send(msg)

def setup(client):
    client.add_cog(SayCommand(client))