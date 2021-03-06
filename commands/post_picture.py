import os
import discord
from config import config
from handle_messages import delete_user_message
from cmd_manager.filters import is_ex_yuri_channel, is_ex_yaoi_channel, is_ex_trap_channel
from cmd_manager.decorators import register_command

yuri_folder = config.PICTURE.yuri
yaoi_folder = config.PICTURE.yaoi
trap_folder = config.PICTURE.trap
spam_folder = config.PICTURE.spam


async def send_picture(client, folder, channel_id):
    for i in os.listdir(folder):
        channel = client.get_channel(channel_id)
        try:
            await client.send_file(channel, folder + i)
            os.remove(folder + i)
            return
        except discord.HTTPException:
            os.remove(folder + i)
            print("Error: File to large")


@register_command('yuri', is_enabled=is_ex_yuri_channel, description='Post a yuri picture.')
async def yuri(client, message, args):
    await delete_user_message(message)
    await send_picture(client, yuri_folder, "328616388233265154")


@register_command('trap', is_enabled=is_ex_trap_channel, description='Post a trap picture.')
async def trap(client, message, args):
    await delete_user_message(message)
    await send_picture(client, trap_folder, "356169435360264192")


@register_command('yaoi', is_enabled=is_ex_yaoi_channel, description='Post a yaoi picture.')
async def yaoi(client, message, args):
    await delete_user_message(message)
    await send_picture(client, yaoi_folder, "328942447784624128")


@register_command('miles', is_enabled=None, description='Post the miles picture.')
async def miles(client, message, args):
    await delete_user_message(message)
    await client.send_file(message.channel, spam_folder + "miles.jpg", content=f"From: {message.author.display_name}")


@register_command('paid', is_enabled=None, description='Post the getting_paid picture.')
async def paid(client, message, args):
    await delete_user_message(message)
    await client.send_file(message.channel, spam_folder + "getting_paid.jpg", content=f"From: {message.author.display_name}")
