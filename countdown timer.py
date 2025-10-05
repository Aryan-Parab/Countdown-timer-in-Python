import time
def main():
    y = int(input("What's the time in seconds?  "))
    for i in range(y, 0,-1):  
        seconds = i % 60
        minutes = int(i/ 60) %60
        hours = int(i / 24) % 24
        print(f"00:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print("times up")
main()
