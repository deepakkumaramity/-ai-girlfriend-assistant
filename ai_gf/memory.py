history = []

def add_user(msg):
    history.append({"role": "user", "content": msg})

def add_ai(msg):
    history.append({"role": "assistant", "content": msg})

def get_history():
    return history[-20:]