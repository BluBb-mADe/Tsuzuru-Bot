import discord
from handle_messages import private_msg
from handle_messages import delete_user_message
from cmd_manager.decorators import register_command, add_argument
from cmd_manager.filters import is_ex_fan_release_channel, command_not_allowed


@register_command('post_fansub', is_enabled=is_ex_fan_release_channel, description='Post your release in #release_fansubs.')
@add_argument('name', help='Your group + anime name.')
@add_argument('episode', help='Episode number + name')
@add_argument('--link', '-l', dest='links', nargs=2, required=True, action='append', help='Links.', metavar=("Name", "Link"))
async def post_fansub(client, message, args):
    await delete_user_message(message)

    title = f"{args.name}"
    description = f"{args.episode}"
    for lname, link in args.links:
        if len(lname) > 6:
            lname = lname[:6]
        if not link.startswith("http"):
            await private_msg(message, "Cant find http link.")
            return
        description += f" [{lname}]({link}) ||"

    embed = discord.Embed(title=title, description=description[:-3], color=0x000000)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    channel = client.get_channel("221920731871707136")
    await client.send_message(channel, embed=embed)


# TODO Rewrite for new arg_parse system.
# TODO atm disabled.
@register_command('multi_fansub', is_enabled=command_not_allowed, description='Post your release in #release_fansubs.')
@add_argument('name', help='Your group + anime name.')
@add_argument('--episode', '-e', nargs="+", action="append", help='Episode + Names/Links ....... Names/Links')
async def multi_fansub(client, message, args):
    await delete_user_message(message)

    title = f"{args.name}"
    description = f"{args.episode}"
    for lname, link in args.links:
        if len(lname) > 6:
            lname = lname[:6]
        if not link.startswith("http"):
            await private_msg(message, "Cant find http link.")
            return
        description += f" [{lname}]({link}) ||"

    embed = discord.Embed(title=title, description=description[:-3], color=0x000000)
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    channel = client.get_channel("221920731871707136")
    await client.send_message(channel, embed=embed)