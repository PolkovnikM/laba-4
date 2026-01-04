print("4. ПРОКСИ: Защита игрового сервера")


class GameServer:
    def __init__(self):
        print("Сервер: Запускаю игровой мир...")

    def send_command(self, player, command):
        print(f"Сервер: Игрок '{player}' выполнил '{command}'")
        return f"Результат: {command} успешно"


class ServerProxy:
    def __init__(self, server):
        self.server = server
        self.banned_players = ["хакер123", "читер_про"]
        self.command_history = []

    def send_command(self, player, command):
        # Проверка бана
        if player in self.banned_players:
            return f"Игрок {player} забанен!"

        if "delete" in command.lower() or "crash" in command.lower():
            return "Опасная команда отклонена!"

        self.command_history.append(f"{player}: {command}")
        print(f"Прокси: Логирую команду от {player}")

        if len(self.command_history) > 5:
            recent = self.command_history[-5:]
            if all(cmd.startswith(player) for cmd in recent[-3:]):
                return "Слишком много команд! Подождите..."
        return self.server.send_command(player, command)


server = GameServer()
proxy = ServerProxy(server)

players = [
    ("Windblowes", "move north"),
    ("linikerhd", "delete all items"),
    ("новичок", "attack enemy"),
    ("новичок", "use potion"),
    ("новичок", "open chest"),
    ("новичок", "equip sword"),
]

for player, command in players:
    print(f"\n{player} → {command}")
    result = proxy.send_command(player, command)
    print(result)