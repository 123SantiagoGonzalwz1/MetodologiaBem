class Person():
    def __init__(self, name):
        self._name = name

class Group():
    def __init__(self, members, subgroups):
        self._members = members
        self._subgroups = subgroups

def get_all(group):
    sub_members = []
    for subgroup in group._subgroups:
        sub_members.extend(get_all(subgroup))

    return group._members + sub_members

group = Group(['Byte', 'Key'], [Group(['Ice Cream', 'Toothsie'], [] )])

print(get_all(group))
