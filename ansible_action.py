import subprocess
import json
def run_command_with_ansible(inventory_file, command, user):
    """Run a command on remote servers using Ansible."""
    ansible_cmd = [
        'ansible', 
        'all', 
        '-i', inventory_file, 
        '-u', user, 
        '-m', 'shell', 
        '-a', command
    ]
    
    try:
        result = subprocess.run(ansible_cmd, capture_output=True, text=True, check=True)
        output = json.loads(result.stdout)
        return output
    except subprocess.CalledProcessError as e:
        print(f"Ansible command failed: {e.stderr}")
        return None
def run_ansible_command_vault(inventory_file, credentials_file, command):
    """Run an Ansible command with the given inventory and credentials."""
    ansible_cmd = [
        "ansible", 
        "all", 
        "-i", inventory_file, 
        "--vault-password-file", credentials_file, 
        "-m", "shell", 
        "-a", command
    ]
    
    try:
        result = subprocess.run(ansible_cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Ansible command failed: {e.stderr}"
