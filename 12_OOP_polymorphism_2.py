class Hill:
    def height(self):
        height = 100
        print(f"height of the hill is {height} ")

    def location(self):
        town = "Badulla"
        print(f"The hill is located in {town} ")

class Town:
    def height(self):
        height = 200
        print(f"Height of the tower is {height} ")

    def location(self):
        town = "Colombo"
        print(f"The town is located in {town}")

# for i in [Hill(), Town()]:
#     i.height(), i.location()

[(i.height(), i.location()) for i in [Hill(), Town()]]