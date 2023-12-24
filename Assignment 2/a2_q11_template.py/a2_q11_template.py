tree = {
 'Amy': 'Ben', 'Tom': 'Ben' , 'Frank' : 'Amy',
 'May': 'Tom', 'Ben': 'Howard', 'Howard': 'George'
}

tree2 = {
 'Amy' : 'Ben' , 'Tom' : 'Ben' , 'Frank' : 'Amy',
 'May' : 'Tom' , 'Ben' : 'Howard', 'Howard': 'George',
 'Joe' : 'Bill' , 'Bill' : 'Mary' , 'Zoe' :'Mary',
 'Mary': 'Philip', 'Simon': 'Bill'
}

def find_ancestor(name, t):
    # You may assume that name belongs to the ancestry tree
    # Every name in the Dictionary is unique
    # Every person has at most one parent
    # There will be no cycle
    ancestor = name
    while True:
        try:
            ancestor = t[ancestor]

        except KeyError:
            return ancestor

def is_related(name1, name2, t):
     if find_ancestor(name1, t) == find_ancestor(name2, t):
         return True
     else:
         return False       

