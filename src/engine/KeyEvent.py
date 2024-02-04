def IsPressing(window, key):
    if key in window.KeyDown:
        return True
    return False
