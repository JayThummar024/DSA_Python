class Treenode:
    def __init__(self,data):
        self.parent = None
        self.data = data
        self.children = []

    def add_child(self,child):
       child.parent = self
       self.children.append(child)

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            level+=1
            p = p.parent
        return level

    def print_tree(self):
        space = " " * self.get_level() * 3
        prefix = space + "|__"
        print(prefix + self.data if self.parent else "" + self.data)
        for child in self.children:
            child.print_tree()

#above class is to create normal tree

node = Treenode("Electronics")

laptop = Treenode("Laptop")
tv = Treenode("Tv")
mobile =Treenode("Mobile")

lenovo=Treenode("Lenovo")
dell=Treenode("dell")
hp=Treenode("hp")

onePlus = Treenode("OnePlus")
Akai = Treenode("Akai")

mi = Treenode("Mi")
realme = Treenode('Realme')
samsung = Treenode("Samsung")

laptop.add_child(lenovo)
laptop.add_child(dell)
laptop.add_child(hp)

tv.add_child(onePlus)
tv.add_child(Akai)
mobile.add_child(samsung)

mobile.add_child(mi)
mobile.add_child(realme)

node.add_child(laptop)
node.add_child(tv)
node.add_child(mobile)

node.print_tree()


