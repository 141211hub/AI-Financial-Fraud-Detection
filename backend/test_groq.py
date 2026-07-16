from pathlib import Path
from dotenv import dotenv_values

env_path = Path(__file__).parent / ".env"

print("Exists:", env_path.exists())

print("Raw file:")
print(repr(env_path.read_text()))

print("\nParsed:")
print(dotenv_values(env_path))