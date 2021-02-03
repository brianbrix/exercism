def convert(number):
    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    result = "".join([sounds[x] for x in sounds.keys() if not number % x])
    if len(result) < 1:
        result = str(number)
    return result
