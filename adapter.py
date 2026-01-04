print(" 6. АДАПТЕР: Системы измерений")

class ImperialSystem:

    def get_height_ft(self):
        return "Рост: 6 футов 2 дюйма"

    def get_weight_lbs(self):
        return "Вес: 180 фунтов"

    def get_temp_f(self):
        return "Температура: 98.6°F"

    def get_distance_mi(self):
        return "Расстояние: 5 миль"

class MetricSystem:

    def get_height_m(self):
        return "Рост: 1.88 метра"

    def get_weight_kg(self):
        return "Вес: 81.6 кг"

    def get_temp_c(self):
        return "Температура: 37°C"

    def get_distance_km(self):
        return "Расстояние: 8 километров"

class OldRussianSystem:

    def get_height_arshin(self):
        return "Рост: 2 аршина 12 вершков"

    def get_weight_russian_pound(self):
        return "Вес: 10 пудов"

    def get_temp_re(self):
        return "Температура: 29.6°Ré"

    def get_distance_verst(self):
        return "Расстояние: 3 версты"

class UniversalMeasurements:

    def get_height(self):
        pass

    def get_weight(self):
        pass

    def get_temperature(self):
        pass

    def get_distance(self):
        pass

class ImperialAdapter(UniversalMeasurements):
    def __init__(self, imperial_system):
        self.imperial = imperial_system

    def get_height(self):
        height_str = self.imperial.get_height_ft()
        ft_inch = height_str.split(": ")[1]
        ft, inch = ft_inch.split(" футов ")
        inch = inch.replace(" дюйма", "")
        total_inches = int(ft) * 12 + int(inch)
        meters = total_inches * 0.0254

        return f"Рост: {ft_inch} ≈ {meters:.2f} м"

    def get_weight(self):
        weight_str = self.imperial.get_weight_lbs()
        lbs = int(weight_str.split(": ")[1].replace(" фунтов", ""))
        kg = lbs * 0.453592

        return f"Вес: {lbs} фунтов ≈ {kg:.1f} кг"

    def get_temperature(self):
        temp_str = self.imperial.get_temp_f()
        f = float(temp_str.split(": ")[1].replace("°F", ""))
        c = (f - 32) * 5 / 9

        return f"Температура: {f}°F ≈ {c:.1f}°C"

    def get_distance(self):
        dist_str = self.imperial.get_distance_mi()
        miles = float(dist_str.split(": ")[1].replace(" миль", ""))
        km = miles * 1.60934

        return f"Расстояние: {miles} миль ≈ {km:.1f} км"

class MetricAdapter(UniversalMeasurements):
    def __init__(self, metric_system):
        self.metric = metric_system

    def get_height(self):
        return self.metric.get_height_m()

    def get_weight(self):
        return self.metric.get_weight_kg()

    def get_temperature(self):
        return self.metric.get_temp_c()

    def get_distance(self):
        return self.metric.get_distance_km()

class OldRussianAdapter(UniversalMeasurements):
    def __init__(self, russian_system):
        self.russian = russian_system

    def get_height(self):
        height_str = self.russian.get_height_arshin()
        parts = height_str.split(": ")[1].split(" аршина ")
        arshin = int(parts[0])
        vershok = int(parts[1].replace(" вершков", ""))
        total_m = arshin * 0.7112 + vershok * 0.04445

        return f"Рост: {arshin} арш. {vershok} верш. ≈ {total_m:.2f} м"

    def get_weight(self):
        weight_str = self.russian.get_weight_russian_pound()
        pood = int(weight_str.split(": ")[1].replace(" пудов", ""))
        kg = pood * 16.38

        return f"Вес: {pood} пудов ≈ {kg:.1f} кг"

    def get_temperature(self):
        temp_str = self.russian.get_temp_re()
        re = float(temp_str.split(": ")[1].replace("°Ré", ""))

        c = re * 1.25

        return f"Температура: {re}°Ré ≈ {c:.1f}°C"

    def get_distance(self):
        dist_str = self.russian.get_distance_verst()
        verst = float(dist_str.split(": ")[1].replace(" версты", "").replace(" верст", ""))
        km = verst * 1.0668

        return f"Расстояние: {verst} верст ≈ {km:.1f} км"


class MeasurementDisplay:

    def show_measurements(self, system):
        print(f"Измерения ({system.__class__.__name__}):")
        print("-" * 40)
        print(system.get_height())
        print(system.get_weight())
        print(system.get_temperature())
        print(system.get_distance())



print("Перевод между разными системами измерений:")

imperial = ImperialSystem()
metric = MetricSystem()
russian = OldRussianSystem()

imperial_adapter = ImperialAdapter(imperial)
metric_adapter = MetricAdapter(metric)
russian_adapter = OldRussianAdapter(russian)

display = MeasurementDisplay()

display.show_measurements(imperial_adapter)
display.show_measurements(metric_adapter)
display.show_measurements(russian_adapter)

print("БЕЗ АДАПТЕРА:")
try:
    display.show_measurements(imperial)
except Exception as e:
    print(f"Ошибка: {type(e).__name__}")
    print("Нужен адаптер для конвертации в единый формат!")

print("КОНВЕРТАЦИЯ НА ЛЕТУ:")
print("180 фунтов →", imperial_adapter.get_weight())
print("10 пудов →", russian_adapter.get_weight())
print("98.6°F →", imperial_adapter.get_temperature())