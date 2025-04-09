from union_find_algorithm import initialize, union, find, are_in_same_group

def draw_tree(parent):
    print("\nStruktura e parent[] si pemë:")
    for i, p in enumerate(parent):
        arrow = "→" if i != p else "↻"  # ↻ = rrënja e vetes
        print(f"  {i} {arrow} {p}")

def print_state(parent, rank, label):
    print(f"\n🟦 {label}")
    print("Parent array:", parent)
    print("Rank array:  ", rank)
    draw_tree(parent)

def main():
    print("💻 Testim vizual i Union-Find me 6 përdorues")
    parent, rank = initialize(6)
    print_state(parent, rank, "Gjendja fillestare")

    union(parent, rank, 0, 1)
    union(parent, rank, 1, 2)
    print_state(parent, rank, "Pas union(0,1) dhe union(1,2)")

    union(parent, rank, 3, 4)
    union(parent, rank, 4, 5)
    print_state(parent, rank, "Pas union(3,4) dhe union(4,5)")

    print("\n🔍 Kontrollime:")
    print("A janë 0 dhe 2 në të njëjtin grup? =>", are_in_same_group(parent, 0, 2))  # True
    print("A janë 0 dhe 5 në të njëjtin grup? =>", are_in_same_group(parent, 0, 5))  # False

    union(parent, rank, 0, 5)
    print_state(parent, rank, "Pas union(0,5) - Bashkim i dy grupeve")

    print("\n✅ Kontroll përfundimtar:")
    print("A janë 0 dhe 5 në të njëjtin grup? =>", are_in_same_group(parent, 0, 5))  # True

if __name__ == "__main__":
    main()

