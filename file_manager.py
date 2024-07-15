import os
from datetime import datetime

def get_items(directory):
    """Gets a list of files and folders within the given directory."""
    return [os.path.join(directory, item) for item in os.listdir(directory)]

def rename_items(directory):
    """Interactively renames files or folders in the given directory."""

    items = get_items(directory)
    if not items:
        print("No items found in the directory.")
        return

    print("\nItems in the directory:")
    for i, item in enumerate(items):
        print(f"{i+1}. {item}")

    choice = int(input("\nChoose an option:\n1. Rename a specific item\n2. Rename all items with a pattern\n3. Rename all items with the current date\nYour choice: "))

    if choice == 1:
        item_index = int(input("Enter the number of the item to rename: ")) - 1
        if 0 <= item_index < len(items):
            old_path = items[item_index]
            new_name = input("Enter the new name: ")
            directory, _ = os.path.split(old_path)  # Extract directory from old path
            new_path = os.path.join(directory, new_name)  # Construct new path within the same directory
            os.rename(old_path, new_path)
            print(f"Renamed '{old_path}' to '{new_path}'")
        else:
            print("Invalid item number.")

    elif choice == 2:
        new_name_pattern = input("Enter the new name pattern (use {counter} and/or {original_name}): ")
        for i, item in enumerate(items):
            directory, filename = os.path.split(item)  # Extract directory and filename
            base_name, extension = os.path.splitext(filename)
            new_name = new_name_pattern.format(counter=i+1, original_name=base_name) + extension
            new_path = os.path.join(directory, new_name)  # Construct new path within the same directory
            os.rename(item, new_path)
            print(f"Renamed '{item}' to '{new_path}'")

    elif choice == 3:
        today = datetime.today().strftime("%Y-%m-%d")
        for item in items:
            directory, filename = os.path.split(item)  # Extract directory and filename
            base_name, extension = os.path.splitext(filename)
            new_name = f"{base_name}_{today}{extension}"
            new_path = os.path.join(directory, new_name)  # Construct new path within the same directory
            os.rename(item, new_path)
            print(f"Renamed '{item}' to '{new_path}'")

    else:
        print("Invalid choice.")
