from config import dp, start
from text_utils import match_with
from aiogram.types import Message
from parser import get_dict


@dp.message_handler(match_with(regexp=r'[\w-]+'))
async def test(msg: Message):
    word = msg.text
    await msg.answer(str(get_dict(word)))


start()
