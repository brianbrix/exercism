def two_fer(name=""):
    try:
        if name:
            return "One for {}, one for me.".format(name)
        else:
            return "One for you, one for me."
    except (Exception, TypeError) as e:
        raise Exception(e)
