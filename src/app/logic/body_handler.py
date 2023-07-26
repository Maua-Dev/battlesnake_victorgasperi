def avoid_body(body, next_movement):
    to_remove = []
    
    for direction, future_position in next_movement.items():
        if future_position in body:
            to_remove.append(direction)
    
    to_remove = set(to_remove)
    for direction in to_remove:
        del next_movement[direction]    
    
    return next_movement
