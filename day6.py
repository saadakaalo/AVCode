mem_banks = [11, 11, 13, 7, 0, 15, 5, 
             5, 4, 4, 1, 1, 7, 1, 15, 11]

all_banks = []

while mem_banks not in all_banks:
    max_val = max(mem_banks)
    max_val_index = mem_banks.index(max_val)
    n_vals = len(mem_banks)
    add_val_each = max_val//n_vals

    all_banks.append(mem_banks)

    print(max_val_index)
