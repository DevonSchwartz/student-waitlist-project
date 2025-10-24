'''
Find the index of the username from waitlist or return -1 if username is not in waitlist
Pre Conditions: 0 <= len(waitlist)
Post Conditions: 
if the username is in waitlist, return the index of that user so that 0 <= index < len(waitlist) 
if the username is not in the waitlist, return -1
'''
def getPosition(username : str, waitlist : list[str]) -> int:
    pass

'''
Remove the person at the front of the waitlist or return None if the waitlist si empty
PreConditions: 0 <= len(waitlist)
Post Conditions:
if len(waitlist) > 0 then return the name of the person at waitlist[0] and remove waitlist[0] from waitlist
if len(waitlist) == 0 then return None
'''
def popFront(waitlist: list[str]) -> str:
    pass 

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
    pass 


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
    pass 


'''
Return a string reprsentation of the waitlist in the following format
[Position]:[Username]
[Position]:[Username]
...
[Last Position] : [Username]
This should use 1-index instead of 0-index
If the waitlist is emtpy, return "Waitlist Empty"
Pre: 0 <= len(waitlist)
Post: 
len(waitlist) > 0 : return string representation of waitlist
len(waitlist) == 0: return "Waitlist Empty"
'''
def printWaitlist(waitlist: str) -> str:
    pass 
