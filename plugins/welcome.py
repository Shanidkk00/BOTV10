import os
from pyrogram import Client, filters
from pyrogram.types import Message, User



@Client.off_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Welcome {message.from_user.mention} to {message.chat.username} ,  Happy to have here",chat_id=chatid)
	
@Client.off_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Bye ,  {message.from_user.mention} , Have a Nice Day",chat_id=chatid)
	

