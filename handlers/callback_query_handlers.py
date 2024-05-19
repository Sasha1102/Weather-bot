def register(bot):
    @bot.callback_query_handler(func=lambda call: call.data == 'menu')
    def menu(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data == 'profile')
    def profile(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data == 'weather_by_coordinates')
    def weather_by_coordinates(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data == 'distribution')
    def distribution(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data == 'change_city')
    def change_city(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'time')
    def choose_time(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'duration')
    def choose_time(call):
        pass