user_dict = {}

def put_user_answer(from_id, right_answer):
    try:
        user_dict[from_id] = right_answer
    except:
        pass
    return

def get_user_answer(from_id):
    try:
        return user_dict[from_id]
    except:
        return False
