def convert(number):
    ob = {3: "Pling", 5: "Plang", 7: "Plong"}
    f = "".join([ob[x] for x in ob.keys() if number % x == 0])
    if len(f) < 1:
        f = str(number)
    return f


