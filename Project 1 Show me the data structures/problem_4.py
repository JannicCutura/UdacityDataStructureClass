class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name




def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    for member in group.get_users():
        if user == member:
            return True
    for subgroup in group.get_groups():
        return is_user_in_group(user, subgroup)

    return False

myfamily = Group("MyFamily")
children = Group("children")
pets = Group("pets")
myfamily.add_user("Me")
myfamily.add_user("girlfriend")

children.add_user("Anna")
children.add_user("Paul")

pets.add_user("Cat")
pets.add_user("Dog")


myfamily.add_group(children)
myfamily.add_group(pets)
myfamily.get_groups()


print(is_user_in_group("Me",myfamily))
# True

print(is_user_in_group("Anna",myfamily))
# True

print(is_user_in_group("Marcus",myfamily))
# False

print(is_user_in_group("cat",myfamily))
# True


print(is_user_in_group("",myfamily))
# False

print(is_user_in_group(" ",myfamily))
# False

print(is_user_in_group(None,myfamily))
# False






