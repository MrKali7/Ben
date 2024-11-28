from config import BOT_DIRS, SESSIONS
import subprocess

def run_bots():
    processes = []

    for dir, session in zip(BOT_DIRS, SESSIONS):
        print(f"Starting bot in {dir} with session {session}")
        try:
            process = subprocess.Popen(
                ["python3", "main.py", session],
                cwd=dir
            )
            processes.append(process)
        except Exception as e:
            print(f"Error: Failed to start bot in {dir} - {e}")
            exit(1)

    for process in processes:
        process.wait()

    print("All bots are running.")

if __name__ == "__main__":
    run_bots()


