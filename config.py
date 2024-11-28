import os

# Define environment variables with defaults
REPOS = [
    os.getenv("BOT1_REPO", "https://github.com/MrKali7/custompro2.git"),
    os.getenv("BOT2_REPO", "https://github.com/MrKali7/custompro3.git")
]

BOT_DIRS = [
    os.getenv("BOT1_DIR", "custompro2"),
    os.getenv("BOT2_DIR", "custompro3")
]

SESSIONS = [
    os.getenv("BOT1_SESSION", "bot1_session"),
    os.getenv("BOT2_SESSION", "bot2_session")
]

# Optional: Add other configurations (e.g., ports, database settings)
EXPOSED_PORTS = [
    os.getenv("BOT1_PORT", "8080"),
    os.getenv("BOT2_PORT", "9090")
]
