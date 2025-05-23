import time

def stopwatch():
    print("⏱️ Simple Stopwatch")
    print("Press [Enter] to start...")
    input()
    start_time = time.time()
    print("Stopwatch started. Press [Enter] to stop.")
    input()
    end_time = time.time()

    elapsed = end_time -start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    milliseconds = int((elapsed - int(elapsed)) * 1000)

    print(f"\n⏱ Elapsed time: {minutes}m {seconds}s {milliseconds}ms")
    
def countdown(seconds):
    print(f"\n⏳ Countdown starting for {seconds} seconds...")
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up!")


if __name__ == "__main__":
    choice = input("Start stopwatch or countdown? (s/c): ").lower()
    if choice == 's':
        stopwatch()
    elif choice == 'c':
        try:
            secs = int(input("Enter countdown time in seconds: "))
            countdown(secs)
        except ValueError:
            print("❌ Invalid input.")
    else:
        print("Invalid choice.")