import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
    return result.stdout.strip()

# Step 1: Configure Git
git_name = input("Enter your GitHub name: ")
git_email = input("Enter your GitHub email (use your private GitHub email if applicable): ")

print("\nConfiguring Git...")
run_command(f'git config --global user.name "{git_name}"')
run_command(f'git config --global user.email "{git_email}"')
run_command('git config --global init.defaultBranch main')
run_command('git config --global pull.rebase false')

# Step 2: Verify Git configuration
print("\nVerifying Git configuration...")
print(run_command('git config --get user.name'))
print(run_command('git config --get user.email'))

# Step 3: Ignore .DS_Store files (for macOS users)
if os.name == 'posix':
    print("\nConfiguring Git to ignore .DS_Store files...")
    run_command('echo .DS_Store >> ~/.gitignore_global')
    run_command('git config --global core.excludesfile ~/.gitignore_global')

# Step 4: Generate SSH key if not exists
ssh_key_path = os.path.join(os.path.expanduser("~"), ".ssh", "id_ed25519.pub")
private_key_path = os.path.join(os.path.expanduser("~"), ".ssh", "id_ed25519")

# Make sure the .ssh directory exists
if not os.path.exists(os.path.dirname(private_key_path)):
    os.makedirs(os.path.dirname(private_key_path))

if not os.path.exists(ssh_key_path):
    print("\nGenerating a new SSH key...")
    keygen_command = f'ssh-keygen -t ed25519 -f "{private_key_path}" -N ""'
    run_command(keygen_command)
else:
    print("\nSSH key already exists.")

# Step 5: Display the SSH public key
if os.path.exists(ssh_key_path):
    print("\nYour SSH public key (Copy this and add it to GitHub):")
    read_command = f'cat "{ssh_key_path}"' if os.name != 'nt' else f'type "{ssh_key_path}"'
    print(run_command(read_command))
else:
    print("\nError: SSH key generation failed or not found.")

print("\nNow, go to GitHub, and add this public key to your SSH keys in Settings > SSH and GPG keys.")
