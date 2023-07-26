def get_head_coordinates(request: dict):
    return request["you"]["head"]

def get_body_coordinates(request: dict):
    return request["you"]["body"]

def get_board_height(request: dict):
    return request["board"]["height"]

def get_board_width(request: dict):
    return request["board"]["width"]

def get_other_snakes_coordinates(request: dict):
    return request["board"]["snakes"]

def get_food_coordinates(request: dict):
    return request["board"]["food"]
