s = list(input("What do you want to check for being a palindrome?"))
sLower = s.casefold()
sFinal = ""
for s in [*s]:
    if s.isalpha(): sFinal += s.lower()
    if s.isnumeric(): sFinal += s
if sFinal == sFinal[::-1]:
    print("True")
else:
    print("False")
