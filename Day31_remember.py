from pathlib import Path 
import json 

name = input("Name")
path = Path('username.json')
contents = json.dumps(name)
path.write_text(contents)

print(f"Your name is remember {name}")
