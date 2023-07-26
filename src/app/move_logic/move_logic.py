import random
from ..body_handler.body_handler import avoid_body
from ..food_handler.food_handler import closest_food, get_food
from ..snakes_handler.other_snakes_handler import avoid_snake
from ..walls_handler.walls_handler import avoid_wall
from ..request_handler.request_handler import get_board_height, get_board_width, get_body_coordinates, get_food_coordinates, get_head_coordinates, get_other_snakes_coordinates
from ..next_movement.set_next_movement import set_next_movement_dict

#evitar colidir com o proprio corpo
#evitar colidir com a parede
#randomizar os movimentos restantes


def choose_direction(request: dict) -> str:

    my_head = get_head_coordinates(request)
    my_body = get_body_coordinates(request)
    board_height = get_board_height(request)
    board_width = get_board_width(request)
    other_snakes = get_other_snakes_coordinates(request)
    food = get_food_coordinates(request)

    next_movement = set_next_movement_dict(my_head)

    next_movement = avoid_body(my_body, next_movement)
    next_movement = avoid_wall(board_width, board_height, next_movement)
    next_movement = avoid_snake(other_snakes, next_movement)
    closest_food_possible = closest_food(food, my_head)

    if(len(next_movement) == 0):
        move = "down"
    else: 
        if closest_food_possible is not None:
            move = get_food(next_movement, my_head, closest_food_possible)
        else:
            next_movement = list(next_movement.keys())
            move = random.choice(next_movement)

    print(move)
    
    return move



