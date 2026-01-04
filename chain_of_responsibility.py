print("2. ЦЕПОЧКА: Техподдержка игрового сервера")


class SupportHandler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, problem):
        if self.next_handler:
            return self.next_handler.handle(problem)
        return "❌ Проблему не смогли решить"


class Level1Support(SupportHandler):
    def handle(self, problem):
        if problem == "не загружается игра":
            return "Уровень 1: Попробуйте перезапустить лаунчер"
        elif problem == "зависло меню":
            return "Уровень 1: Нажмите Alt+F4 и зайдите снова"
        else:
            return super().handle(problem)


class Level2Support(SupportHandler):
    def handle(self, problem):
        if problem == "вылетает на загрузке":
            return "Уровень 2: Обновите драйвера видеокарты"
        elif problem == "лаги в игре":
            return "Уровень 2: Понизьте настройки графики"
        else:
            return super().handle(problem)


class Level3Support(SupportHandler):
    def handle(self, problem):
        if problem == "потеря сохранения":
            return "Уровень 3: Восстанавливаем из облака..."
        elif problem == "баг с квестами":
            return "Уровень 3: Разработчики уже фиксят"
        else:
            return "Уровень 3: Отправляем специалиста"

level1 = Level1Support()
level2 = Level2Support()
level3 = Level3Support()

level1.set_next(level2)
level2.set_next(level3)


problems = [
    "не загружается игра",
    "лаги в игре",
    "потеря сохранения",
    "неизвестная ошибка"
]

for problem in problems:
    print(f"\nПроблема: {problem}")
    print(f"Решение: {level1.handle(problem)}")