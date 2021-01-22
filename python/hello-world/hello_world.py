def hello():
    try:
        return "Hello, World!"
    except Exception as e:
        raise Exception(e)
