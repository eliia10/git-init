def validate_input(func):
    def wrapper(initial_velocity, final_velocity, time):
        try:
            initial_velocity = float(initial_velocity)
            final_velocity = float(final_velocity)
            time = float(time)
            if time == 0:
                raise ValueError("Время не может быть равно нулю.")
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")
            return None
        
        acceleration = func(initial_velocity, final_velocity, time)

        distance = (initial_velocity + final_velocity) / 2 * time
        print(f"Пройденное расстояние: {distance} м")
        
        return acceleration
    
    return wrapper

@validate_input
def calculate_acceleration(initial_velocity, final_velocity, time):
    return (final_velocity - initial_velocity) / time

a = float(input('Начальная скорость: '))
b = float(input('Конечная скорость: '))
c = float(input('Время: '))

acceleration = calculate_acceleration(a, b, c)
if acceleration is not None:
    print(f"Ускорение: {acceleration} м/с²")
