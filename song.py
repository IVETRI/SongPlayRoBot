import os
import time
import ffmpeg
import logging
import requests
import youtube_dl
from pyrogram import filters, Client, idle
from youtube_search import YoutubeSearch
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


## Commands --------
@Client.on_message(filters.command(['start']))
async def start(client, message):
       await message.reply("𝐈'𝐦 𝐡𝐞𝐥𝐩𝐢𝐧𝐠 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐲𝐨𝐮𝐫 𝐥𝐨𝐯𝐞𝐥𝐲 𝐬𝐨𝐧𝐠𝐬 𝐨𝐧 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦🎸🎸🎸.[🎶](https://fzstream.techwizardent.com/70785)𝐃𝐨 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐤𝐧𝐨𝐰 𝐦𝐨𝐫𝐞 𝐚𝐛𝐨𝐮𝐭 𝐦𝐞 𝐡𝐢𝐭 𝐭𝐡𝐞 @ElizaSupporters.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🔔', url='https://t.me/Updates_of_ElizaBot'),
                    InlineKeyboardButton('𝐒𝐞𝐚𝐫𝐜𝐡 𝐈𝐧𝐥𝐢𝐧𝐞', switch_inline_query_current_chat='')
                ]
            ]
        )
    )

@Client.on_message(filters.command(['help']))
async def help(client, message):
       await message.reply("<b>𝐇𝐢𝐭 𝐡𝐞𝐥𝐩 𝐛𝐮𝐭𝐭𝐨𝐧 𝐭𝐨 𝐟𝐢𝐧𝐝 𝐦𝐨𝐫𝐞 𝐚𝐛𝐨𝐮𝐭 𝐡𝐨𝐰 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞... 𝐒𝐞𝐧𝐝 - /help </i>\n\n<b>Eg</b> `/song Faded`",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Developer', url='https://t.me/SehathSanvidu')
                ]
            ]
        )
    )

@Client.on_message(filters.command(['about']))
async def about(client, message):
       await message.reply("➪<b>Name</b> : ✫<i>Song Downloader</i>\n➪<b>Developer</b> : ✫[SehathPerera](https://t.me/SehathSanvidu)\n➪<b>Language</b> : ✫<i>Python3</i>\n➪<b>Server</b> : ✫[𝘏𝘦𝘳𝘰𝘬𝘶](https://heroku.com/)\n➪<b>Source Code</b> : ✫[𝘊𝘭𝘪𝘤𝘬 𝘏𝘦𝘳𝘦](https://github.com/PereraSehath)",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Search Inline', switch_inline_query_current_chat='')
                ]
            ]
        )
    )

@Client.on_message(filters.text)
def a(client, message):
    query=message.text
    print(query)
    m = message.reply('🔎 𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐒𝐨𝐧𝐠...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            performer = f"MusicDownloadv2bot" 
            views = results[0]["views"]
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('𝐒𝐨𝐫𝐫𝐲 𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝 𝐘𝐨𝐮𝐫 𝐒𝐨𝐧𝐠!!!')
            return
    except Exception as e:
        m.edit(
            "❎ 𝐹𝑜𝑢𝑛𝑑 𝑁𝑜𝑡ℎ𝑖𝑛𝑔.\n\nEg.`Faded`"
        )
        print(str(e))
        return
    m.edit("`𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐒𝐨𝐧𝐠, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭...`")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep =  f'🎧 𝗧𝗶𝘁𝘁𝗹𝗲 : [{title[:35]}]({link})\n⏳ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 : `{duration}`\n👀 𝐕𝐢𝐞𝐰𝐬 : `{views}`\n\n📮 𝗕𝘆: {message.from_user.mention()}\n📤 𝗕𝘆 : @AnnieElizaSongDT_Bot'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('𝐅𝐚𝐢𝐥𝐞𝐝\n\n`𝐏𝐥𝐞𝐚𝐬𝐞 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 𝐋𝐚𝐭𝐞𝐫...`')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
