def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == "key" and child.text == key:
            found = True
    return None
