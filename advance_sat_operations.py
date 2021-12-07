# set ... use {} carily bracket

art_friend = {"santo", "doba", "shuvo"}
science_friend = {"apurba", "santo",}

art_but_not_sience = art_friend.difference(science_friend)
science_but_not_sience = science_friend.difference(art_friend)
print(art_but_not_sience)
print(science_but_not_sience)

not_in_both = art_friend.symmetric_difference(science_friend)
print(not_in_both)

art_and_science = art_friend.intersection(science_friend)
print(art_and_science)


all_friend = art_friend.union(science_friend)
print(all_friend)