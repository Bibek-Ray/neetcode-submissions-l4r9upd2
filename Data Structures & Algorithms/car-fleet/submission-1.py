class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stk = []
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars = sorted(cars)

        for i in range(len(position) - 1, -1, -1):
            current_car_time = (target - cars[i][0])/cars[i][1]
            if len(stk) != 0:
                last_car_time = stk[-1]

                if current_car_time > last_car_time:
                    stk.append(current_car_time)

            else:
                stk.append(current_car_time)

        return len(stk)