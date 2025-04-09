from union_find_algorithm import initialize, union, find, are_in_same_group

def print_state(parent, rank, label):
    print(f"\n--- {label} ---")
    print("Parent:", parent)
    print("Rank:  ", rank)

def main():
    # Hapi 1: Inicializimi
    parent, rank = initialize(6)
    print_state(parent, rank, "Gjendja fillestare")

    # Hapi 2: Bashkimet
    union(parent, rank, 0, 1)
    union(parent, rank, 1, 2)
    print_state(parent, rank, "Pas union(0,1) dhe union(1,2)")

    union(parent, rank, 3, 4)
    union(parent, rank, 4, 5)
    print_state(parent, rank, "Pas union(3,4) dhe union(4,5)")

    # Hapi 3: Kontrollo nëse janë në të njëjtin grup
    print("\nKontrollime:")
    print("A janë 0 dhe 2 në të njëjtin grup?", are_in_same_group(parent, 0, 2))  # True
    print("A janë 0 dhe 5 në të njëjtin grup?", are_in_same_group(parent, 0, 5))  # False

    # Hapi 4: Bashko të dy grupet
    union(parent, rank, 0, 5)
    print_state(parent, rank, "Pas union(0,5) - bashkim i dy grupeve të mëdha")
    print("A janë 0 dhe 5 në të njëjtin grup?", are_in_same_group(parent, 0, 5))  # True

if __name__ == "__main__":
    main()
