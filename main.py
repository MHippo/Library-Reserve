import hikari, miru, arc
import asyncio
import ping3
import tomllib
import math
from promptgenv3 import Promptgen

promptgen = Promptgen()
print(promptgen.generate_ham_prompt("o5"))

bot = hikari.GatewayBot(token=open("token.txt", "r").read().strip())
client = arc.GatewayClient(bot)

@client.include
@arc.slash_command("ping", "Responds with Pong and the current latency")
async def ping_command(ctx: arc.Context):
    if ctx.author.id != 910236925842042930:
        latency = ping3.ping("discord.com", unit="ms")
        await ctx.respond(f"Pong! Latency: {math.floor(latency)} ms")
    else:
        await ctx.respond("Ping this dick in your ass tri")


@client.include
@arc.slash_command("rprompt", "Generates a prompt based on the specified rank")
async def prompt_command(ctx: arc.Context, rank: arc.Option[str, arc.StrParams("Rank", choices=["Library Liability", "Scribe", "Scholar", "Librarian", "Lorekeeper", "Knowledge Seeker"])]):
        if ctx.author.id != 910236925842042930:
            prompt = promptgen.generate_ham_prompt(rank)
            print(prompt)
            text = "\n  ".join(prompt)
            await ctx.respond(f"{rank}:\n  {text}")
        else:
            await ctx.respond("no prompts for you loser")

@client.include
@arc.slash_command("groom", "grooms deeoon")
async def groom_command(ctx: arc.Context):
    if ctx.author.id != 910236925842042930:
        await ctx.respond("<@840189706340007938> you're so mature for your age~")
    else:
        await ctx.respond("fuck you")

@client.include
@arc.slash_command("ham", "calls ham a bitch")
async def ham_command(ctx: arc.Context):
    if ctx.author.id != 910236925842042930:
        await ctx.respond("<@674801593501089802> you a bitch")
    else:
        await ctx.respond("<@910236925842042930> you a bitch")


@client.include
@arc.slash_command("prompt")
async def prompt_command(ctx: arc.Context, mono: arc.Option[bool, arc.BoolParams("Mono Attunement?")]):
    if ctx.author.id != 910236925842042930:
        prompt = promptgen.generate_prompt(mono=mono)
        print(prompt)
        await ctx.respond(f"Prompt:\n  {prompt}")
    else:
        await ctx.respond("FUCK no. I aint doing SHIT for you.")

@client.include
@arc.slash_command("fixthebot")
async def fix_the_bot_command(ctx: arc.Context):
    if ctx.author.id != 910236925842042930:
        await ctx.respond("Fix The Bot <@457197127723122688>")
    else:
        await ctx.respond("dont tell him to do shit nigga")

bot.run()