'''
Find the index of the username from waitlist or return -1 if username is not in waitlist
Pre Conditions: 0 <= len(waitlist)
Post Conditions: 
if the username is in waitlist, return the index of that user so that 0 <= index < len(waitlist) 
if the username is not in the waitlist, return -1
'''
def getPosition(username : str, waitlist : list[str]) -> int:
    for i in range(len(waitlist)):
        if waitlist[i] == username:
            return i
    return -1

'''
Remove the person at the front of the waitlist or return None if the waitlist si empty
PreConditions: 0 <= len(waitlist)
Post Conditions:
if len(waitlist) > 0 then return the name of the person at waitlist[0]
and remove the element at waitlist[0]
if len(waitlist) == 0 then return None
'''
def popFront(waitlist: list[str]) -> str:
    if len(waitlist) == 0:
        return None
    return waitlist.pop(0) 

'''
Add username to the waitlist if getPosition(username) == -1
Pre Conditions: 0 <= len(waitlist)
Post Conditions:
if the username isn't in waitlist, waitlist is mutated so that at the end of the function,
waitlist[len(waitlist) - 1] == username. In addition, return True
if username is in waitlist, return False. len(waitlist) at the end of the function equals the 
len(waitlist) at the beginning of the function
'''
def addUsername(username: str, waitlist : list[str]) -> bool:
    if getPosition(username, waitlist) == -1:
        waitlist.append(username)
        return True
    return False

'''
Remove the username from waitlist if username is in waitlist and return True if the username
was removed and False otherwise
Pre Condition: 0 <= len(waitlist)
Post Conditions:
if the username isn't in waitlist, return False. len(waitlist) at the end of the function 
equals the len(waitlist) at the beginning of the function
if the username is in waitlist, waitlist is mutated so that at the end of the function, 
the size of the waitlist is decreased by 1 and username not in waitlist. In addition, return True
'''
def removeUsername(username : str, waitlist : list[str]) -> bool:
    for i in range(len(waitlist)):
        if waitlist[i] == username:
            waitlist.pop(i)
            return True
    return False


'''
Return a string reprsentation of the waitlist in the following format
[Position]:[Username]
[Position]:[Username]
...
[Last Position] : [Username]
This should output Position as 1-index instead of 0-index
If the waitlist is emtpy, return "Waitlist Empty"
Pre: 0 <= len(waitlist)
Post: 
len(waitlist) > 0 : return string representation of waitlist
len(waitlist) == 0: return "Waitlist Empty"
'''
def printWaitlist(waitlist: str) -> str:
    output = []

    for i in range(len(waitlist)):
        output.append(f"{i + 1} {waitlist[i]}")

    return '\n'.join(output)
