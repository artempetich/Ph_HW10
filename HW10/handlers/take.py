import random
from loader import dp
from aiogram.types import Message
import game
from game import total_dic, set_total




    
    
    
@dp.message_handler()
async def mes_help(message: Message):
    
    global total_dic
    if set_total[message.from_user.id] == True:
        try:
            int(message.text)
            total_dic[message.from_user.id] = int(message.text)
            print(total_dic[message.from_user.id])
            await message.answer(f"Вы положили на стол {int(message.text)}. Сколько конфет хотите взять?")
            set_total[message.from_user.id] = False
        except ValueError:
            await message.answer("Это Вы что положили на стол? {message.text}? Нужно число.")
    elif message.from_user.id in total_dic.keys():
        count = message.text
        if count.isdigit() and 0 < int(count) < 29:
            total_dic[message.from_user.id] -= int(count)
            if await check_win(message, message.from_user.first_name):
                return True
            await message.answer(f'{message.from_user.first_name} взял {count} конфет и на столе осталось {total_dic[message.from_user.id]}\n'
                                 f'Теперь ход бота...')
            bot_take = random.randint(1, 28) if total_dic[message.from_user.id] > 28 else total_dic[message.from_user.id]
            total_dic[message.from_user.id] -= bot_take
            if await check_win(message, 'Бот'):
                return True
            await message.answer(f'Бот Виталий взял {bot_take} конфет и '
                                 f'на столе осталось {total_dic[message.from_user.id]}\n'
                                 f'Теперь твой ход...')
        else:
            await message.answer(f'Введите число от 1 до 28')


async def check_win(message: Message, win: str):
    global total_dic
    global set_total
    if total_dic[message.from_user.id] <= 0:
        await message.answer(f'{win} победил! Поздравляю!')
        # game.total.remove(duel)
        # game.total_dic.pop(message.from_user.id)
        total_dic.pop(message.from_user.id)
        set_total[message.from_user.id] = False
        return True
    return False