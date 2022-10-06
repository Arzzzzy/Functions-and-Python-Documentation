#def to_share(total_candies, n_friends=4):
    #return total_candies % n_friends

#print(to_share(91))
#print(to_share(91, 3))


def to_share(total_candies, n_friends=3):
    return total_candies % n_friends

print(to_share(91))
print(to_share(10, 4))
print(to_share(5))
print(to_share(1, 5))



