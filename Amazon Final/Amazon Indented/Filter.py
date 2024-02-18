def fl(name):
    if name.isalnum():
        return True
    else:
        if name == " ":
            return True
        else:
            return False


def af(name):
    f = filter(fl, name)
    s = ""
    for g in f:
        s += g
    return (s)

