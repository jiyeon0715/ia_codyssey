def read_csv_file(filename):
    inventory = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                parts = line.strip().split(',')
                
                if index == 0:
                    continue  

                try:
                    name = parts[0].strip()
                    flammability = float(parts[-1].strip())
                    inventory.append((name, flammability))
                except ValueError:
                    print(f'Invalid data format: {line.strip()}')

    except FileNotFoundError:
        print(f'Error: File {filename} not found.')  
    except Exception as e:
        print(f'Error reading file: {e}')  
    
    print(f"Final inventory list ({len(inventory)} items): {inventory}")  
    return inventory

def save_csv_file(filename, data):
    try:
        with open(filename, 'w') as file:
            for name, flammability in data:
                file.write(f'{name},{flammability}\n')
    except Exception as e:
        print(f'Error writing file: {e}')

def save_binary_file(filename, data):
    try:
        with open(filename, 'wb') as file:
            for name, flammability in data:
                file.write(f'{name},{flammability}\n'.encode())
    except Exception as e:
        print(f'Error writing binary file: {e}')

def read_binary_file(filename):
    try:
        with open(filename, 'rb') as file:
            content = file.read().decode()
            print('\n=== Binary File Contents ===')
            print(content)
    except FileNotFoundError:
        print(f'Error: File {filename} not found.')
    except Exception as e:
        print(f'Error reading binary file: {e}')

def main():
    csv_filename = 'Mars_Base_Inventory_List.csv'
    danger_csv_filename = 'Mars_Base_Inventory_danger.csv'
    binary_filename = 'Mars_Base_Inventory_List.bin'
    
    inventory = read_csv_file(csv_filename)
    if not inventory:
        return
    
    inventory_sorted = sorted(inventory, key=lambda x: x[1], reverse=True)
    
    dangerous_items = [item for item in inventory_sorted if item[1] >= 0.7]
    
    print('\n=== Sorted Inventory ===')
    for item in inventory_sorted:
        print(item)
    
    print('\n=== Dangerous Items (flammability >= 0.7) ===')
    for item in dangerous_items:
        print(item)
    
    save_csv_file(danger_csv_filename, dangerous_items)
    
    save_binary_file(binary_filename, inventory_sorted)
    read_binary_file(binary_filename)
    
if __name__ == '__main__':
    main()
