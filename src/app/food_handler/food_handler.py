from scipy import spatial

def closest_food(foods, head):
    food_positions = []

    if len(foods) == 0:
        return None

    for food in foods:
        food_positions.append( (food["x"], food["y"]) )
    
    tree = spatial.KDTree(food_positions)

    tree_query = tree.query([(head["x"], head["y"])])[1]

    return foods[tree_query[0]]

def get_food(next_movement, head, food_position):
    previous_distance_x = abs(head["x"] - food_position["x"])
    previous_distance_y = abs(head["y"] - food_position["y"])

    for direction, future_position in next_movement.items():
        future_distance_x = abs(future_position["x"] - food_position["x"])
        future_distance_y = abs(future_position["y"] - food_position["y"])

        if future_distance_x < previous_distance_x or future_distance_y < previous_distance_y:
            return direction
        
    return list(next_movement.keys())

def check_if_has_eaten(food_position, head, health):
    previous_health = health
    if head["x"] == food_position["x"] and head["y"] == food_position["y"]:
        if previous_health < health:
            return True
        else:
            return False
