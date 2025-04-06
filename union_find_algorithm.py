import time
import sys
import random

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

def measure_memory_usage(parent, rank):
    # Mat perdorimin e memories per listat parent dhe rank
    return sys.getsizeof(parent) + sys.getsizeof(rank)

def run_performance_tests(num_users, num_operations):
    # Krijon strukturat fillestare
    parent, rank = initialize(num_users)
    
    # Gjeneron operacione te rastesishme union
    union_operations = [(random.randint(0, num_users - 1), random.randint(0, num_users - 1)) for _ in range(num_operations)]
    find_operations = [random.randint(0, num_users - 1) for _ in range(num_operations)]
    
    # Mat kohen per operacionet union
    start_time = time.time()
    for user1, user2 in union_operations:
        union(parent, rank, user1, user2)
    union_time = time.time() - start_time
    
    # Mat kohen per operacionet find
    start_time = time.time()
    for user in find_operations:
        find(parent, user)
    find_time = time.time() - start_time
    
    # Mat perdorimin e memories
    memory_usage = measure_memory_usage(parent, rank)
    
    return {
        "num_users": num_users,
        "num_operations": num_operations,
        "union_time": union_time,
        "find_time": find_time,
        "memory_usage": memory_usage
    }

def main():
    # Teston algoritmin me raste te ndryshme te madhesise se te dhenave
    test_cases = [
        (100, 500),    # Rast i vogel
        (1000, 5000),  # Rast mesatar
        (10000, 50000) # Rast i madh
    ]
    
    results = []
    for num_users, num_operations in test_cases:
        result = run_performance_tests(num_users, num_operations)
        results.append(result)
        print(result)  # Printon rezultatet per analize

if __name__ == "__main__":
    main()
