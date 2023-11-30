# Tool for checking whether a gift is pog or not
# @author Sarah Robertson
# @date 11-29-2023

import functions as f

print("=== GIFT GUIDE ===")
print()
print("*** Beta version: includes ALEX, HALEY, SEBASTIAN, MARNIE, and WIZARD ***")
print()
print("Type exit to quit at any time")
print()
def main():
    while True: #character loop
        name = input(str("Enter character name: "))
        if name == "exit":
            f.done()
        else:
            while True:
                check = f.check_name(name)
                if name == "exit":
                    f.done()
                elif check:
                    break
                else:
                    name = input(str("Enter character name: "))
            print()
            print("Type 0 to return to character select")
            print()
            while True:
                gift = input(str("Enter gift name: "))
                if gift == "exit":
                    f.done()
                elif gift == "0":
                    break
                else:
                    f.check(name, gift)
        

main()