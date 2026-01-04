print("5. МОСТ: Графика в игре")


# Реализация графики
class GraphicsAPI:
    def render_character(self, name):
        pass

    def render_terrain(self):
        pass


class DirectX11(GraphicsAPI):
    def render_character(self, name):
        return f"DirectX11: Рисую {name} с шейдерами"

    def render_terrain(self):
        return "DirectX11: Текстуры ландшафта загружены"


class OpenGL(GraphicsAPI):
    def render_character(self, name):
        return f" OpenGL: {name} в высоком разрешении"

    def render_terrain(self):
        return " OpenGL: Ландшафт с тенью"


class Vulkan(GraphicsAPI):
    def render_character(self, name):
        return f"Vulkan: {name} с RTX-отражениями"

    def render_terrain(self):
        return "Vulkan: Ультра-детализированный мир"


# Игровые объекты
class GameObject:
    def __init__(self, graphics):
        self.graphics = graphics

    def draw(self):
        pass


class Player(GameObject):
    def __init__(self, name, graphics):
        super().__init__(graphics)
        self.name = name

    def draw(self):
        return self.graphics.render_character(self.name)


class World(GameObject):
    def draw(self):
        return self.graphics.render_terrain()


# Играем с разной графикой
print("\nЗапускаем игру на разных API:")

apis = [DirectX11(), OpenGL(), Vulkan()]

for api in apis:
    print(f"\n--- {api.__class__.__name__} ---")
    player = Player("Эльф-воин", api)
    world = World(api)

    print(player.draw())
    print(world.draw())

    # Меняем графику на лету
    if isinstance(api, DirectX11):
        player.graphics = Vulkan()
        print(" Переключаемся на Vulkan!")
        print(player.draw())