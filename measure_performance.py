import time
import sys
import matplotlib.pyplot as plt
from union_find_algorithm import initialize, find, union, are_in_same_group

def measure_performance(num_users, num_operations):
    parent, rank = initialize(num_users)
    
    start_time_union = time.time()
    for _ in range(num_operations):
        user1, user2 = _ % num_users, (_ * 2) % num_users  
        union(parent, rank, user1, user2)
    end_time_union = time.time()
    
    start_time_find = time.time()
    for _ in range(num_operations):
        user1 = _ % num_users
        find(parent, user1)
    end_time_find = time.time()
    
    memory_usage = sys.getsizeof(parent) + sys.getsizeof(rank)

    # Shto printimet për të parë rezultatet
    print(f"Numri i Përdoruesve: {num_users}, Numri i Operacioneve: {num_operations}")
    print(f"Koha për union(): {end_time_union - start_time_union:.6f} s")
    print(f"Koha për find(): {end_time_find - start_time_find:.6f} s")
    print(f"Përdorimi i Memories: {memory_usage} bytes")
    print("-" * 50)  # Vizon ndarëse për qartësi
    
    return (end_time_union - start_time_union, end_time_find - start_time_find, memory_usage)

# Testo me madhësi të ndryshme
users_sizes = [100, 1000, 10000]
operations_per_test = [500, 5000, 50000]
results = [measure_performance(users, ops) for users, ops in zip(users_sizes, operations_per_test)]

# Vizualizimi i rezultateve
union_times = [res[0] for res in results]
find_times = [res[1] for res in results]
memory_usage = [res[2] for res in results]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(users_sizes, union_times, marker='o', label='Union Time (s)')
plt.plot(users_sizes, find_times, marker='s', label='Find Time (s)')
plt.xlabel('Numri i perdoruesve')
plt.ylabel('Koha (s)')
plt.legend()
plt.title('Koha e ekzekutimit e Union dhe Find')

plt.subplot(1,2,2)
plt.plot(users_sizes, memory_usage, marker='^', color='r', label='Memory Usage (bytes)')
plt.xlabel('Numri i perdoruesve')
plt.ylabel('Perdorimi i memories')
plt.legend()
plt.title('Perdorimi i memories')

plt.tight_layout()
plt.show()
