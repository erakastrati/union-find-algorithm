def initialize(num_users):
    # Inicializimi i strukturës së bashkimit
    parent = [i for i in range(num_users)]  # Çdo përdorues është prind i vetes (fillimisht secili është grup më vete)
    rank = [0] * num_users  # Ranku (lartësia e pemës) fillimisht është zero për secilin përdorues
    return parent, rank


def find(parent, user):
    # Gjetja e përfaqësuesit të grupit për një përdorues
    if parent[user] != user:  # Nëse nuk është rrënja, kërko rrënjën
        parent[user] = find(parent, parent[user])  # Kompresimi i shtegut për optimizim
    return parent[user]


def union(parent, rank, user1, user2):
    # Bashkimi i dy grupeve në një
    root1 = find(parent, user1)  # Gjejmë rrënjën e grupit të përdoruesit 1
    root2 = find(parent, user2)  # Gjejmë rrënjën e grupit të përdoruesit 2
    
    # Bashkojmë vetëm nëse janë në grupe të ndryshme
    if root1 != root2:
        # Bashkim sipas rangut: lidhet pema më e vogël me atë më të madhe
        
        # Nëse rrënja e parë ka rang më të madh, bëhet prind i rrënjës së dytë
        if rank[root1] > rank[root2]:
            parent[root2] = root1 
            
        # Nëse rrënja e dytë ka rang më të madh, bëhet prind i rrënjës së parë
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
            
        else:
            # Nëse kanë të njëjtin rang, zgjedhim njërin (root1) si rrënjë dhe rrisim rangun e tij
            parent[root2] = root1  
            rank[root1] += 1  # Rritet rangu i root1, pasi pema e tij bëhet më e thellë


def are_in_same_group(parent, user1, user2):
    # Kontrollon nëse dy përdorues janë në të njëjtin grup
    return find(parent, user1) == find(parent, user2)


# Shembull i thjeshtë për testim

def main():
    num_users = 5  # Numri total i përdoruesve në rrjetin social
    parent, rank = initialize(num_users)  # Inicializimi i strukturës

    # Bashkojmë disa përdorues për të krijuar grupe shoqërore
    union(parent, rank, 0, 1)  # Lidhim përdoruesin 0 me përdoruesin 1
    union(parent, rank, 2, 3)  # Lidhim përdoruesin 2 me përdoruesin 3
    
    # Kontrollojmë nëse përdoruesi 0 dhe 1 janë në të njëjtin grup
    print("A janë përdoruesi 0 dhe 1 në të njëjtin grup?", are_in_same_group(parent, 0, 1))  # Pritet: True
    
    # Kontrollojmë nëse përdoruesi 0 dhe 2 janë në të njëjtin grup
    print("A janë përdoruesi 0 dhe 2 në të njëjtin grup?", are_in_same_group(parent, 0, 2))  # Pritet: False
    
    # Përdoruesi 1 dhe 2 bëhen miq
    union(parent, rank, 1, 2)
    
    # Kontrollojmë përsëri nëse përdoruesi 0 dhe 2 janë në të njëjtin grup
    print("A janë përdoruesi 0 dhe 2 në të njëjtin grup?", are_in_same_group(parent, 0, 2))  # Pritet: True


if __name__ == "__main__":
    main()