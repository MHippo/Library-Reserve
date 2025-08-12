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
    latency = ping3.ping("discord.com", unit="ms")
    await ctx.respond(f"Pong! Latency: {math.floor(latency)} ms")

@client.include
@arc.slash_command("rprompt", "Generates a prompt based on the specified rank")
async def prompt_command(ctx: arc.Context, rank: arc.Option[str, arc.StrParams("Rank", choices=["Library Liability", "scribe", "scholar", "Book Keeper", "Librarian", "Lorekeeper"])]):
    prompt = promptgen.generate_ham_prompt(rank)
    print(prompt)
    text = "\n  ".join(prompt)
    await ctx.respond(f"{rank}:\n  {text}")

@client.include
@arc.slash_command("groom", "grooms deeoon")
async def groom_command(ctx: arc.Context):
    await ctx.respond("<@840189706340007938> you're so mature for your age~")

@client.include
@arc.slash_command("ham", "calls ham a bitch")
async def ham_command(ctx: arc.Context):
    await ctx.respond("<@674801593501089802> you a bitch ass nigga")

@client.include
@arc.slash_command("prompt")
async def prompt_command(ctx: arc.Context, mono: arc.Option[bool, arc.BoolParams("Mono Attunement?")]):
    prompt = promptgen.generate_prompt(mono=mono)
    print(prompt)
    await ctx.respond(f"Prompt:\n  {prompt}")



bot.run()