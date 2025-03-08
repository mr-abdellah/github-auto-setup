import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
    return result.stdout.strip()

git_name = input("Enter your GitHub name: ")
git_email = input("Enter your GitHub email: ")

print("\nConfiguring Git...")
run_command(f'git config --global user.name "{git_name}"')
run_command(f'git config --global user.email "{git_email}"')
run_command('git config --global init.defaultBranch main')
run_command('git config --global pull.rebase false')

ssh_key_path = os.path.join(os.path.expanduser("~"), ".ssh", "id_ed25519.pub")
private_key_path = os.path.join(os.path.expanduser("~"), ".ssh", "id_ed25519")

if not os.path.exists(ssh_key_path):
    print("\nGenerating a new SSH key...")
    keygen_command = f'ssh-keygen -t ed25519 -f "{private_key_path}" -N ""'
    run_command(keygen_command)

if os.path.exists(ssh_key_path):
    print("\nYour SSH public key (Copy this and add it to GitHub):")
    read_command = f'type "{ssh_key_path}"' if os.name == 'nt' else f'cat "{ssh_key_path}"'
    print(run_command(read_command))
else:
    print("\nError: SSH key generation failed or not found.")
