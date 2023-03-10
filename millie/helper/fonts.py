from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 
from millie.helper_functions.fonts_func import Fonts


@Client.on_message(filters.private & filters.command(["font"]))
async def style_buttons(c, m, cb=False):
    buttons = [[
        InlineKeyboardButton('๐๐ข๐๐๐ ๐๐๐๐๐', callback_data='style+typewriter'),
        InlineKeyboardButton('๐๐ฆ๐ฅ๐๐๐๐', callback_data='style+outline'),
        InlineKeyboardButton('๐๐๐ซ๐ข๐', callback_data='style+serif'),
        ],[
        InlineKeyboardButton('๐บ๐๐๐๐', callback_data='style+bold_cool'),
        InlineKeyboardButton('๐๐๐๐๐', callback_data='style+cool'),
        InlineKeyboardButton('Sแดแดสส Cแดแดs', callback_data='style+small_cap'),
        ],[
        InlineKeyboardButton('๐๐ธ๐๐พ๐๐', callback_data='style+script'),
        InlineKeyboardButton('๐ผ๐ฌ๐ป๐ฒ๐น๐ฝ', callback_data='style+script_bolt'),
        InlineKeyboardButton('แตโฑโฟสธ', callback_data='style+tiny'),
        ],[
        InlineKeyboardButton('แOแฐIแ', callback_data='style+comic'),
        InlineKeyboardButton('๐ฆ๐ฎ๐ป๐', callback_data='style+sans'),
        InlineKeyboardButton('๐๐๐ฃ๐จ', callback_data='style+slant_sans'),
        ],[
        InlineKeyboardButton('๐๐ข๐ฏ๐ด', callback_data='style+slant'),
        InlineKeyboardButton('๐ฒ๐บ๐๐', callback_data='style+sim'),
        InlineKeyboardButton('โธ๏ธโพ๏ธโ๏ธโธ๏ธโ๏ธโบ๏ธโ๏ธ', callback_data='style+circles')
        ],[
        InlineKeyboardButton('๐๏ธ๐๏ธ๐ก๏ธ๐๏ธ๐๏ธ๐๏ธ๐ข๏ธ', callback_data='style+circle_dark'),
        InlineKeyboardButton('๐๐ฌ๐ฑ๐ฅ๐ฆ๐ ', callback_data='style+gothic'),
        InlineKeyboardButton('๐ฒ๐๐๐๐๐', callback_data='style+gothic_bolt'),
        ],[
        InlineKeyboardButton('Cอกอlอกอoอกอuอกอdอกอsอกอ', callback_data='style+cloud'),
        InlineKeyboardButton('Hฬฬaฬฬpฬฬpฬฬyฬฬ', callback_data='style+happy'),
        InlineKeyboardButton('Sฬฬaฬฬdฬฬ', callback_data='style+sad'),
        ],[
        InlineKeyboardButton('Next โก๏ธ', callback_data="nxt")
    ]]
    if not cb:
        if ' ' in m.text:
            title = m.text.split(" ", 1)[1]
            await m.reply_text(title, reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=m.id)                     
        else:
            await m.reply_text(text="Ente Any Text Eg:- `/font [text]`")    
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex('^nxt'))
async def nxt(c, m):
    if m.data == "nxt":
        buttons = [[
            InlineKeyboardButton('๐ธโ๐ตโ๐ชโ๐จโ๐ฎโ๐ฆโ๐ฑโ', callback_data='style+special'),
            InlineKeyboardButton('๐๐๐๐ฐ๐๐ด๐', callback_data='style+squares'),
            InlineKeyboardButton('๐๏ธ๐๏ธ๐๏ธ๐ฐ๏ธ๐๏ธ๐ด๏ธ๐๏ธ', callback_data='style+squares_bold'),
            ],[
            InlineKeyboardButton('๊ช๊ชแฆ๊ช๊ชถ๊ชแฅด๐ฒ๊ช', callback_data='style+andalucia'),
            InlineKeyboardButton('็ชๅๅ แๅ', callback_data='style+manga'),
            InlineKeyboardButton('Sฬพtฬพiฬพnฬพkฬพyฬพ', callback_data='style+stinky'),
            ],[
            InlineKeyboardButton('Bอฆฬฅuอฆฬฅbอฆฬฅbอฆฬฅlอฆฬฅeอฆฬฅsอฆฬฅ', callback_data='style+bubbles'),
            InlineKeyboardButton('Uอnอdอeอrอlอiอnอeอ', callback_data='style+underline'),
            InlineKeyboardButton('๊๊๊ท๊ฉ๊๊๊', callback_data='style+ladybug'),
            ],[
            InlineKeyboardButton('Rาaาyาsา', callback_data='style+rays'),
            InlineKeyboardButton('Bาiาrาdาsา', callback_data='style+birds'),
            InlineKeyboardButton('Sฬธlฬธaฬธsฬธhฬธ', callback_data='style+slash'),
            ],[
            InlineKeyboardButton('sโ tโ oโ pโ ', callback_data='style+stop'),
            InlineKeyboardButton('Sอฬบkอฬบyอฬบlอฬบiอฬบnอฬบeอฬบ', callback_data='style+skyline'),
            InlineKeyboardButton('Aอrอrอoอwอsอ', callback_data='style+arrows'),
            ],[
            InlineKeyboardButton('แชแแญแฟแ', callback_data='style+qvnes'),
            InlineKeyboardButton('Sฬถtฬถrฬถiฬถkฬถeฬถ', callback_data='style+strike'),
            InlineKeyboardButton('Fเผrเผoเผzเผeเผnเผ', callback_data='style+frozen')
            ],[
            InlineKeyboardButton('โฌ๏ธ Back', callback_data='nxt+0'),
            InlineKeyboardButton('๐ Close', callback_data='close_data')
        ]]
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        await style_buttons(c, m, cb=True)

@Client.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    if style == 'typewriter':
        cls = Fonts.typewriter
    if style == 'outline':
        cls = Fonts.outline
    if style == 'serif':
        cls = Fonts.serief
    if style == 'bold_cool':
        cls = Fonts.bold_cool
    if style == 'cool':
        cls = Fonts.cool
    if style == 'small_cap':
        cls = Fonts.smallcap
    if style == 'script':
        cls = Fonts.script
    if style == 'script_bolt':
        cls = Fonts.bold_script
    if style == 'tiny':
        cls = Fonts.tiny
    if style == 'comic':
        cls = Fonts.comic
    if style == 'sans':
        cls = Fonts.san
    if style == 'slant_sans':
        cls = Fonts.slant_san
    if style == 'slant':
        cls = Fonts.slant
    if style == 'sim':
        cls = Fonts.sim
    if style == 'circles':
        cls = Fonts.circles
    if style == 'circle_dark':
        cls = Fonts.dark_circle
    if style == 'gothic':
        cls = Fonts.gothic
    if style == 'gothic_bolt':
        cls = Fonts.bold_gothic
    if style == 'cloud':
        cls = Fonts.cloud
    if style == 'happy':
        cls = Fonts.happy
    if style == 'sad':
        cls = Fonts.sad
    if style == 'special':
        cls = Fonts.special
    if style == 'squares':
        cls = Fonts.square
    if style == 'squares_bold':
        cls = Fonts.dark_square
    if style == 'andalucia':
        cls = Fonts.andalucia
    if style == 'manga':
        cls = Fonts.manga
    if style == 'stinky':
        cls = Fonts.stinky
    if style == 'bubbles':
        cls = Fonts.bubbles
    if style == 'underline':
        cls = Fonts.underline
    if style == 'ladybug':
        cls = Fonts.ladybug
    if style == 'rays':
        cls = Fonts.rays
    if style == 'birds':
        cls = Fonts.birds
    if style == 'slash':
        cls = Fonts.slash
    if style == 'stop':
        cls = Fonts.stop
    if style == 'skyline':
        cls = Fonts.skyline
    if style == 'arrows':
        cls = Fonts.arrows
    if style == 'qvnes':
        cls = Fonts.rvnes
    if style == 'strike':
        cls = Fonts.strike
    if style == 'frozen':
        cls = Fonts.frozen

    r, oldtxt = m.message.reply_to_message.text.split(None, 1) 
    new_text = cls(oldtxt)            
    try:
        await m.message.edit_text(f"`{new_text}`\n\n๐ Click To Copy", reply_markup=m.message.reply_markup)
    except Exception as e:
        print(e)
