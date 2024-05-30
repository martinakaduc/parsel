class Group: 
    def __init__(self, members, happinessLevel): 
        self.members = members 
        self.numMembers = len(members) 
        self.happinessLevel = happinessLevel  
    def __repr__(self): 
        return "Group(" + str(self.members) + ", " + str(self.happinessLevel) + ")"    
        
class Member: 
    def __init__(self, name, happinessLevel): 
        self.name = name 
        self.happinessLevel = happinessLevel 
    def __repr__(self): 
        return "Member(\"" + self.name + "\", " + str(self.happinessLevel) + ")"

#*#*#
splitGroups(members, numMembers, standardLevel): Given an array of members and a standard "Happiness level", write a function to group members into as many groups as possible so that the group's "Happiness level" is greater than or equal to the standard "Happiness level" (meets standard). A group has at least 1 member. Know that the "Happiness level" of a group will be the sum of the "Happiness level" of the members in that group. There may exist a group whose "Happiness level" is less than the standard "Happiness level". After grouping, the names of members of groups with a qualified "Happiness level" will be added with the phrase "Happy " at the beginning of the name. For example, "Andy" will become "Happy Andy". The result of this function will be an array containing only groups satisfying "Happiness level" standards, regardless of order. If there is no member, the function returns None. Given the Group and Member classes as below. class Group: def __init__(self, members, happinessLevel): self.members = members self.numMembers = len(members) self.happinessLevel = happinessLevel  def __repr__(self): return "Group(" + str(self.members) + ", " + str(self.happinessLevel) + ")"    class Member: def __init__(self, name, happinessLevel): self.name = name self.happinessLevel = happinessLevel  def __repr__(self): return "Member(\"" + self.name + "\", " + str(self.happinessLevel) + ")"
[Member("Andy", 5)], 1, 6 -> []
[Member("Bob", 7)], 1, 6 -> [Group([Member("Happy Bob", 7)], 7)]
