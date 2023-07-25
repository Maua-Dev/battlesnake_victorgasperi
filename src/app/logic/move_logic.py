from scipy import spatial
import random

#evitar colidir com o proprio corpo
#evitar colidir com a parede
#randomizar os movimentos restantes

def avoid_body(body, next_movement):
    to_remove = []
    
    for direction, future_position in next_movement.items():
        if future_position in body:
            to_remove.append(direction)
    
    to_remove = set(to_remove)
    for direction in to_remove:
        del next_movement[direction]    
    
    return next_movement

def avoid_wall(board_width, board_height, next_movement):
    to_remove = []

    for direction, future_position in next_movement.items():
        right_out_range = future_position["x"] == board_width
        left_out_range = future_position["x"] < 0

        up_out_range = future_position["y"] == board_height
        down_out_range = future_position["y"] < 0

        if right_out_range:
            to_remove.append(direction)
        elif left_out_range:
            to_remove.append(direction)
        elif up_out_range:
            to_remove.append(direction)
        elif down_out_range:
            to_remove.append(direction)

    to_remove = set(to_remove)
    for direction in to_remove:
        del next_movement[direction]
    
    return next_movement

def avoid_snake(snakes_position, next_movement):
    to_remove = []

    for snake in snakes_position:
        for direction, future_position in next_movement.items():
            if future_position in snake["body"]:
                to_remove.append(direction)                       

    to_remove = set(to_remove)    
    for direction in to_remove:
        del next_movement[direction]
    
    return next_movement

def closest_food(foods, head):
    food_positions = []

    if len(foods) == 0:
        return None

    for food in foods:
        food_positions.append(food["x"], food["y"])
    
    tree = spatial.KDTree(food_positions)

    tree_query = tree.query([(head["x"], head["y"])])[1]

    return foods[tree_query[0]]

def choose_direction(request: dict) -> str:

    my_head = request["you"]["head"]
    my_body = request["you"]["body"]
    board_height = request["board"]["height"]
    board_width = request["board"]["width"]
    other_snakes = request["board"]["snakes"]
    food = request["board"]["food"]

    next_movement = {
        "up": {
            "x": my_head["x"],
            "y": my_head["y"] + 1,
        },
        "down": {
            "x": my_head["x"],
            "y": my_head["y"] - 1,
        },
        "right": {
            "x": my_head["x"] + 1,
            "y": my_head["y"],
        },
        "left": {
            "x": my_head["x"] - 1,
            "y": my_head["y"],
        }
    }

    next_movement = avoid_body(my_body, next_movement)
    next_movement = avoid_wall(board_width, board_height, next_movement)
    next_movement = avoid_snake(other_snakes, next_movement)
    closest_food_possible = closest_food(food, my_head)

    next_movement = list(next_movement.keys())
    if(len(next_movement) == 0):
        move = "down"
    
    move = random.choice(next_movement)
    print(move)
    
    return move



