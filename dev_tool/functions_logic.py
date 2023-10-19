import json
import os
import time
import sys
import shutil
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
    config_data["docker_repo"] = "us-east1-docker.pkg.dev/igneous-impulse-396009/streamzero/"

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


def build_image_with_all_modules():

    modules_to_build = get_config()["existing_modules"]

    for module in modules_to_build:
        module_version = update_module_version(module)
        build_tar_gz(module)
        copy_to_templates(module_version)
        update_dockerfile_module_version(module)

    docker_image = build_docker_image()
    push_image = input("Do you want to push it to its corresponding repo? Y/N: ")
    if push_image == "Y" or push_image == "y":
        os.system("docker push " + docker_image)


def copy_to_templates(module_name):
    # Define the source and destination file paths
    templates_folder = get_config()["streamzero_template_path"]
    modules_folder = get_config()["streamzero_modules_path"]

    source_file = f"{modules_folder}/{module_name.split('-')[0].replace('_', '-')}/dist/{module_name}"
    print("printing source file")
    print(source_file)
    destination_folder = f"{templates_folder}/ferrisapp/provisioning/dist"

    # Copy the file to the destination folder
    shutil.copy(source_file, destination_folder)


def build_module():
    key_to_module = get_formated_modules()

    module_to_build = key_to_module[input("Which module do you want to build (enter number): ")]
    clear_console()
    new_module_name = update_module_version(module_to_build)
    build_tar_gz(module_to_build)
    copy_to_templates(new_module_name)


def build_tar_gz(module):

    current_directory = os.getcwd()

    command = "cd " + get_config()["streamzero_modules_path"] + "/" + module + " && sudo python3 setup.py sdist"
    os.system(command)

    os.system("cd " + current_directory)


# def build_tar_gz(module):
#     try:
#         output = subprocess.check_output(["kubectl", "get", "pods", "--no-headers", "-o", "custom-columns=:metadata.name"])
#         output_str = output.decode("utf-8")
#         pod_lines = output_str.split("\n")
#         for line in pod_lines:
#             if ("-web-") in line:
#                 try:
#                     command = [
#                         "kubectl",
#                         "exec",
#                         line,
#                         "--",
#                         "sh",
#                         "-c",
#                         "cd /app/modules/"+module+" && python3 setup.py sdist"
#                     ]
#                     subprocess.run(command, check=True)
#
#                     print("Module built successfully.")
#                 except subprocess.CalledProcessError as e:
#                     print(f"Error executing command: {e}")
#
#
#     except subprocess.CalledProcessError as e:
#         print(f"Error executing kubectl: {e}")

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

    return f"{module.replace('-', '_')}-{VERSION_MAJOR}.{VERSION_MINOR}.{new_version}.tar.gz"

def default_case():
    print("Invalid choice. Please select 1, 2, or 3.")


def get_formated_modules():
    existing_modules = get_config()["existing_modules"]
    key_to_module = {}

    counter = 1
    for module in existing_modules:
        print(str(counter) + ". " + str(module))
        key_to_module[str(counter)] = module
        counter += 1

    return key_to_module


def get_latest_module(module_name):
    templates_folder = get_config()["streamzero_template_path"]
    directory = f"{templates_folder}/ferrisapp/provisioning/dist"

    # List all files in the directory
    all_files = os.listdir(directory)

    # Filter files that start with "bora"
    module_files = [file for file in all_files if file.startswith(module_name.replace("-","_"))]

    # Ensure there are bora files in the directory
    if not module_files:
        print("No files starting with 'bora' found in the directory.")
    else:
        # Get the latest created file
        latest_module_file = max(module_files, key=lambda file: os.path.getctime(os.path.join(directory, file)))
        # print("Latest 'module' file:", latest_module_file)

    return latest_module_file


def update_dockerfile_module_version(module):
    print("updating dockerfile")
    print(module)

    dockerfile = get_config()["streamzero_template_path"] + "/app.Dockerfile"
    with open(dockerfile, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):

        if line.startswith('COPY ferrisapp/provisioning/dist/'+module.replace('-', '_')):
            latest_module = get_latest_module(module)
            lines[i] = f"COPY ferrisapp/provisioning/dist/{latest_module} /dist\n"

        if line.startswith('RUN pip3 install /dist/'+module.replace('-', '_')):
            latest_module = get_latest_module(module)
            lines[i] = f"RUN pip3 install /dist/{latest_module}\n"

    with open(dockerfile, 'w') as file:
        file.writelines(lines)


def build_image_with_specific_modules():

    existing_modules = get_formated_modules()

    print("\nPlease provide a space separated list of modules you wish to build, for example: 1 5 11")
    modules_to_build = input("Modules to build: ").split(" ")

    for module in modules_to_build:
        module_version = update_module_version(existing_modules[module])
        build_tar_gz(existing_modules[module])
        copy_to_templates(module_version)
        update_dockerfile_module_version(existing_modules[module])

    docker_image = build_docker_image()
    push_image = input("Do you want to push it to its corresponding repo? Y/N: ")
    if push_image == "Y" or push_image == "y":
        os.system("docker push " + docker_image)


def build_docker_image():
    current_directory = os.getcwd()

    dockerfile = get_config()["streamzero_template_path"] + "/app.Dockerfile"
    with open(dockerfile, 'r') as file:
        lines = file.readlines()

    current_image_name = lines[1].split(" ")[1]
    current_image_without_version = current_image_name.split(":")[0]
    current_version = current_image_name.split(":")[1]

    major, minor, patch = map(int, current_version.split('.'))

    patch += 1
    new_version = f"{major}.{minor}.{patch}"

    new_image_name = f"{current_image_without_version}:{new_version}"

    command = "cd " + get_config()["streamzero_template_path"] + " && docker build -f app.Dockerfile -t " + new_image_name + " ."
    os.system(command)

    os.system("cd " + current_directory)


    with open(dockerfile, 'w') as file:
        lines[1] = "# " + new_image_name + "\n"
        file.writelines(lines)

    return new_image_name