try:
    import datetime 
except ImportError:
    print("Please install recommended dependency: datetime")
    quit()
    
#Date/ Time Getter 
def getDT():
    return datetime.datetime.now()

# Date/Time Handler
def datetimeHandling(flag):
    if flag == "time":
        return f"It's currently {datetime.datetime.now().strftime('%H:%M:%S')} {greetingTOD()}"
    elif flag == "date":
        return f"It's currently {datetime.datetime.now().strftime('%d/%m/%Y')}"

# Time of Day dependent Greetings 
def greetingTOD():
    currentDT = getDT().strftime('%H:%M:%S')
    hour = int(currentDT[:2])
    if hour < 12:
        return "Good Morning!"
    if hour >= 12:
        return "Good Afternoon."
    if hour > 16:
        return "Good Evening."