def initialize(num_users):
    # Inicializimi i struktures se bashkimit
    parent = [i for i in range(num_users)]  # Çdo perdorues eshte prind i vetes (fillimisht secili eshte grup me vete)
    rank = [0] * num_users  # Ranku (lartesia e pemes) fillimisht eshte zero per secilin perdorues
    return parent, rank


def find(parent, user):
    # Gjetja e perfaqesuesit te grupit per nje perdorues
    if parent[user] != user:  # Nese nuk eshte rrenja, kerko rrenjen
        parent[user] = find(parent, parent[user])  # Kompresimi i shtegut per optimizim
    return parent[user]


def union(parent, rank, user1, user2):
    # Bashkimi i dy grupeve ne nje
    root1 = find(parent, user1)  # Gjejme rrenjen e grupit te perdoruesit 1
    root2 = find(parent, user2)  # Gjejme rrenjen e grupit te perdoruesit 2
    
    # Bashkojme vetem nese jane ne grupe te ndryshme
    if root1 != root2:
        # Bashkim sipas rangut: lidhet pema me e vogel me ate me te madhe
        
        # Nese rrenja e pare ka rang me te madh, behet prind i rrenjes se dyte
        if rank[root1] > rank[root2]:
            parent[root2] = root1 
            
        # Nese rrenja e dyte ka rang me te madh, behet prind i rrenjes se pare
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
            
        else:
            # Nese kane te njejtin rang, zgjedhim njerin (root1) si rrenje dhe rrisim rangun e tij
            parent[root2] = root1  
            rank[root1] += 1  # Rritet rangu i root1, pasi pema e tij behet me e thelle


def are_in_same_group(parent, user1, user2):
    # Kontrollon nese dy perdorues jane ne te njejtin grup
    return find(parent, user1) == find(parent, user2)


# Shembull i thjeshte per testim

def main():
    num_users = 5  # Numri total i perdoruesve ne rrjetin social
    parent, rank = initialize(num_users)  # Inicializimi i struktures

    # Bashkojme disa perdorues per te krijuar grupe shoqerore
    union(parent, rank, 0, 1)  # Lidhim perdoruesin 0 me perdoruesin 1
    union(parent, rank, 2, 3)  # Lidhim perdoruesin 2 me perdoruesin 3
    
    # Kontrollojme nese perdoruesi 0 dhe 1 jane ne te njejtin grup
    print("A jane perdoruesi 0 dhe 1 ne te njejtin grup?", are_in_same_group(parent, 0, 1))  # Pritet: True
    
    # Kontrollojme nese perdoruesi 0 dhe 2 jane ne te njejtin grup
    print("A jane perdoruesi 0 dhe 2 ne te njejtin grup?", are_in_same_group(parent, 0, 2))  # Pritet: False
    
    # Perdoruesi 1 dhe 2 behen miq
    union(parent, rank, 1, 2)
    
    # Kontrollojme perseri nese perdoruesi 0 dhe 2 jane ne te njejtin grup
    print("A jane perdoruesi 0 dhe 2 ne te njejtin grup?", are_in_same_group(parent, 0, 2))  # Pritet: True


if __name__ == "__main__":
    main()