
def initialize(num_users):
    # initially, each user is their own parent, which means they are all in separate groups (or disjoint sets)
    parent = [i for i in range(num_users)]  
    # each user is at the same level or tree height
    rank = [0] * num_users  
    return parent, rank


def find(parent, user):
    if parent[user] != user:  
        # recursively call find to move up the tree this will eventually reach the root of the group
        parent[user] = find(parent, parent[user])  
    # return the root of the group if the user is their own parent, this means the user is the root of the group
    return parent[user]


def union(parent, rank, user1, user2):

    root1 = find(parent, user1)  

    root2 = find(parent, user2)  
    
    # only perform the union if the users are in different groups
    if root1 != root2:  
        # union by rank: we attach the smaller tree the one with less depth
        
        # if the rank (tree height) of root1 is greater than root2, attach root2's tree to root1
        if rank[root1] > rank[root2]:
            parent[root2] = root1 
            
        # if the rank (tree height) of root2 is greater than root1, attach root1's tree to root2
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
            
        else:
            # if both trees have the same rank make root1 the root of root2's group
            parent[root2] = root1  
            rank[root1] += 1  # increase the rank of root1, as root1's tree becomes deeper


def are_in_same_group(parent, user1, user2):
    if find(parent, user1) == find(parent, user2):
        return True  # users are in the same group
    else:
        return False  # users are in different groups

# a simple example
def main():
    num_users = 5  # total number of users in the social network
    parent, rank = initialize(num_users)

    # Union some users to form friend groups
    union(parent, rank, 0, 1)  
    union(parent, rank, 2, 3)
    
    # Check if user1 and user2 are in the same group
    print("Are user1 and user2 in the same group?", are_in_same_group(parent, 0, 1))  # Expected: True
    
    # Check if user1 and user3 are in the same group
    print("Are user1 and user3 in the same group?", are_in_same_group(parent, 0, 2))  # Expected: False
    
    # User2 and User3 become friends
    union(parent, rank, 1, 2)
    
    print("Are user1 and user3 in the same group?", are_in_same_group(parent, 0, 2))  # Expected: True

if __name__ == "__main__":
    main()
