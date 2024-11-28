from config import REPOS, BOT_DIRS
import subprocess
import os

def run_command(command, cwd=None):
    try:
        subprocess.run(command, cwd=cwd, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{e.cmd}' failed with exit code {e.returncode}")
        exit(1)

def build_bots():
    for repo, dir in zip(REPOS, BOT_DIRS):
        if not os.path.exists(dir):
            print(f"Cloning repository: {repo} into {dir}")
            run_command(f"git clone {repo} {dir}")
        else:
            print(f"Directory {dir} already exists. Pulling latest changes.")
            run_command("git pull", cwd=dir)

        print(f"Installing dependencies for {dir}")
        run_command("pip3 install -r requirements.txt", cwd=dir)

    print("Build process completed successfully.")

if __name__ == "__main__":
    build_bots()
