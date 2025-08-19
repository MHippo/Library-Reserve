import hikari, miru, arc
import asyncio
import ping3
import tomllib
import math
from promptgenv3 import Promptgen


promptgen = Promptgen()
with open("config.toml", "rb") as f:
    config = tomllib.load(f)
    token = config["bot"]["token"]

with open("codes.toml", "rb") as f:
    used_codes = tomllib.load(f)["used_codes"]

bot = hikari.GatewayBot(token=token)
client = arc.GatewayClient(bot)

codes = [
    "IDIDNOTTOUCHTHOSEKIDS"
]


@client.include
@arc.slash_command("ping", "Responds with Pong and the current latency")
async def ping_command(ctx: arc.Context):
    if ctx.author.id != 910236925842042930:
        try:
            latency = ping3.ping("discord.com", unit="ms")
            if latency is not None:
                await ctx.respond(f"Pong! Latency: {math.floor(latency)} ms")
            else:
                await ctx.respond("Pong! (Network unreachable)")
        except Exception as e:
            await ctx.respond("Pong! (Error measuring latency)")
    else:
        await ctx.respond("Ping this dick in your ass tri")


@client.include
@arc.slash_command("rprompt", "Generates a prompt based on the specified rank")
async def prompt_command(ctx: arc.Context, rank: arc.Option[str, arc.StrParams("Rank", choices=["Library Liability", "Scribe", "Scholar", "Librarian", "Lorekeeper", "Knowledge Seeker"])]):
        if ctx.author.id != 910236925842042930:
            prompt = promptgen.generate_ham_prompt(rank)
            text = "\n  ".join(prompt)
            await ctx.respond(f"{rank}:\n  {text}")
        else:
            await ctx.respond("nah, im good")

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

@client.include
@arc.slash_command("code", "put in a secret code for something special")
async def reset_codes_command(ctx: arc.Context, code: arc.Option[str, arc.StrParams("Code")]):
    if ctx.author.id != 910236925842042930:
        if code in codes:
            if code not in used_codes[str(ctx.author.id)]:
                used_codes[str(ctx.author.id)] = code
                await ctx.respond("mwah 😘 <3")
            else:
                await ctx.respond("You have already used a code.")
        else:
            await ctx.respond("invalid Code")
    else:
        await ctx.respond("Fuck you no code for you.")

bot.run()