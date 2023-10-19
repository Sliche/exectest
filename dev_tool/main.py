# cli_tool.py
import os
import functions_logic as funcs  # Import the functions_logic module


def main():
    # Check if config.json file exists
    while True:
        if not os.path.exists("config.json"):
            funcs.create_config_file()

        print("\nSelect an option:\n")
        print("1. Build all modules and new image with them")
        print("2. Build new image with specific modules")
        print("3. Update 'dev_tool' config")
        print("4. Build single module")
        print("9. Exit\n")

        user_input = input("Enter your choice: ").strip()  # Updated input prompt
        if user_input == "9":
            break

        switch = {
            "1": funcs.build_image_with_all_modules,  # Option 1
            "2": funcs.build_image_with_specific_modules,  # Option 2
            "3": funcs.update_config,
            "4": funcs.build_module
        }

        selected_function = switch.get(user_input, funcs.default_case)
        selected_function()


if __name__ == "__main__":
    main()
