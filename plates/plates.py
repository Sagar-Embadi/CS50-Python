def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # plates may contain a maximum of 6 characters and a minimum of 2 characters
    if len(s)<2 or len(s)>6:
        return False
    # plates must start with at least two letters
    if s[0:2].isalpha() == False :
        return False
    # checking for numbers in plates
    i=0
    while i < len(s):
        if s[i].isalpha() == False:
            # The first number used cannot be a '0'
            if s[i] == '0':
                return False
            else:
                break
        i += 1
    # checking for spaces and punctuations
    for c in s:
        if c in ['.', ' ', '?', '!']:
            return False
    # if all cases are true then return true
    return True
main()
