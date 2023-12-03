import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(fun=player.move, key="Up")

# Initially creating 10 car from center to right
cars = []
for _ in range(10):
    cars.append(CarManager(random.randint(0, 250)))

scoreboard = Scoreboard()

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Creating new cars every 6th loop
    loop_count += 1
    if loop_count == 6:
        cars.append(CarManager())
        loop_count = 0

    # Detect collision of turtle with the car
    # Making cars to move
    # Removing cars after the left end
    for car in cars:
        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False
        elif car.xcor() > -320:
            car.move(scoreboard.level)
        else:
            cars.remove(car)
            car.hideturtle()

    # Increase level and reset position after completion of a level
    if player.ycor() >= 280:
        scoreboard.update_level()
        player.reset_position()

screen.exitonclick()
