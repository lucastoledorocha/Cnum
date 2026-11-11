import subprocess

message = input("Commit message [update]: ").strip()
if not message:
    message = "update"

branch = input("Branch name [semana1]: ").strip()
if not branch:
    branch = "semana1"

subprocess.run(["git", "add", "-A"], check=True)

commit = subprocess.run(
    ["git", "commit", "-m", message],
    text=True,
)

if commit.returncode != 0:
    print("Nothing to commit.")

subprocess.run(["git", "push", "origin", branch], check=True)

print(f"Done. Pushed to branch '{branch}'.")