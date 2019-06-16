name = input("Please input the name you want to correct the case on. ")
nameArray = name.split()
suffixArray = ["mc", "le", "m'", "mac", "mic", "'o"]
def capitalize(names, prefixes):
    fullname = ""
    for iterator in names:
        for start in prefixes:
            if start in iterator:
                fullname += f"{iterator[0].upper()}{iterator[1:len(start)].lower()}{iterator[len(start)].upper()}{iterator[len(start) + 1:].lower()} "
        if iterator == names[-1] and iterator in fullname.lower():
            break
        else:
            fullname += f"{iterator[0].upper()}{iterator[1:].lower()} "
    return fullname

print(capitalize(nameArray, suffixArray))
input("Press Enter to close.")