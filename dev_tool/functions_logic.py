import json
import os
import time
import sys
import subprocess


def write_dots(wait_time):
    for _ in range(wait_time):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print("\n")


def list_folders(folder_path):
    directories = [d for d in os.listdir(folder_path) if
                   os.path.isdir(os.path.join(folder_path, d)) and not d.startswith(".")]

    return directories

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def build_all_modules():
    print("You selected Option A")


def save_config(filename, config_data):
    with open(filename, 'w') as config_file:
        json.dump(config_data, config_file, indent=4)


def create_config_file():
    print("\nRunning tool for the first time. Lets create config file, please provide the following...")

    config_data = {}
    config_data["streamzero_template_path"] = input("Streamzero template path: ")
    config_data["streamzero_modules_path"] = input("Streamzero modules path: ")

    print("Generating additional config")
    write_dots(5)

    config_data["existing_modules"] = list_folders(config_data["streamzero_modules_path"])
    print("Config generated, proceeding...")
    write_dots(3)

    with open("config.json", "w") as config_file:
        json.dump(config_data, config_file)

    clear_console()


def get_config():
    with open("config.json", 'r') as config_file:
        return json.load(config_file)

def update_config():
    clear_console()

    try:
        with open("config.json", 'r') as config_file:
            config_data = json.load(config_file)
    except FileNotFoundError:
        return None

    if config_data is not None:
        # Pretty-print JSON data
        pretty_json = json.dumps(config_data, indent=4)
        print("Loaded configuration from 'config.json'\n")
        print("Here is your current configuration:")

        print(pretty_json)
        print("\n")

        while True:
            config_key = input("Key you wish to update or add: ")
            config_value = input("New value: ")
            config_data[config_key] = config_value
            update_again = input("Do you wish to update another key? (Y/N): ")
            if update_again == "N" or update_again == "n":
                save_config("config.json", config_data)
                clear_console()
                print("Your new config")
                print(json.dumps(config_data, indent=4))
                break
    else:
        print("The 'config.json' file does not exist.")


def case_b():
    print("You selected Option C")


def build_image():

    print("korka")



def build_module():
    existing_modules = get_config()["existing_modules"]
    key_to_module = {}

    counter = 1
    for module in existing_modules:
        print(str(counter) + ". " + str(module))
        key_to_module[str(counter)] = module
        counter += 1
    module_to_build = key_to_module[input("Which module do you want to build (enter number): ")]
    clear_console()
    update_module_version(module_to_build)
    build_tar_gz(module_to_build)


def build_tar_gz(module):
    try:
        output = subprocess.check_output(["kubectl", "get", "pods", "--no-headers", "-o", "custom-columns=:metadata.name"])
        output_str = output.decode("utf-8")
        pod_lines = output_str.split("\n")
        for line in pod_lines:
            if ("-web-") in line:
                try:
                    command = [
                        "kubectl",
                        "exec",
                        line,
                        "--",
                        "sh",
                        "-c",
                        "cd /app/modules/"+module+" && python3 setup.py sdist"
                    ]
                    subprocess.run(command, check=True)

                    print("Module built successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error executing command: {e}")


    except subprocess.CalledProcessError as e:
        print(f"Error executing kubectl: {e}")

def update_module_version(module):
    modules_path = get_config()["streamzero_modules_path"]
    # file_path = modules_path + "/" + module +"/"+ module.replace('-', '_') + "/" + "version.py"
    file_path = os.path.join(modules_path, module, module.replace('-', '_'), "version.py")

    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith('VERSION_MAJOR'):
            VERSION_MAJOR = line.split('=')[1].strip()
        if line.startswith('VERSION_MINOR'):
            VERSION_MINOR = line.split('=')[1].strip()
        if line.startswith('VERSION_BUILD'):
            VERSION_BUILD = line.split('=')[1].strip()
            new_version = str(int(VERSION_BUILD) + 1)
            lines[2] = "VERSION_BUILD = " + new_version + "\n"
            break

    # Save the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

    # Print the updated version information
    print(f"New module version: {VERSION_MAJOR}.{VERSION_MINOR}.{new_version}")


def default_case():
    print("Invalid choice. Please select 1, 2, or 3.")
