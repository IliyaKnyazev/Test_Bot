import asyncio
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message

bot = Bot("YOUR TOKEN HERE...", parse_mode="HTML")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
      await message.answer(f"Hello, <b>{message.from_user.first_name}</b>")
    
@dp.message(Command(commands=["rn", "random-number"])) # /rn 1-100
async def get_random_number(message: Message, command: CommandObject):
      a, b = [int(n) for n in command.args.split("-")]
      rnum = random.randint(a, b)
      await message.reply(f"Random number: {rnum}")
      
@dp.message(F.text == "play")
async def play_games(message: Message):
      x = await message.answer_dice(DiceEmoji.BASKETBALL)
      print(x.dice.value)@dp.message()
      
async def echo(message: Message):
      await message.answer(f"I don't underestand u!")
      
async def main():
      await bot.delete_webhook(drop_pending_updates=True)
      await dp.start_polling(bot)

if __name__ == "__main__":
      asyncio.run(main())

