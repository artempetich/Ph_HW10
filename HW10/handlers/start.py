import game
from loader import dp
from aiogram.types import Message
from game import total_dic, set_total

@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == set_total[message.from_user.id] :
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
    #     game.new_game = True
        await message.answer(f'Привет, {message.from_user.full_name}'
                             f'Мы будем играть в конфеты. Бери от 1 до 28...'
                             'Введите количество конфет на столе. ')
    #     my_game = [message.from_user.id, message.from_user.first_name, 150]
    #     game.total.append(my_game)
        total_dic[message.from_user.id] = 150
        set_total[message.from_user.id] = True