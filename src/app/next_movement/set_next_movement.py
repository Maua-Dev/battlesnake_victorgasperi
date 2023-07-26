def set_next_movement_dict(my_head):
    return { 
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