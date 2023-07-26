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
