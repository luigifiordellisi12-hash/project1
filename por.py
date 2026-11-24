class ArtGallery:
    def __init__(self, gallery_name, city):
        # TODO 1
        self.gallery_name = gallery_name
        self.city = city
        self.artworks = []
        print(f"{self.gallery_name} in {self.city} is open.")

    def add_artwork(self, title):
        # TODO 2
        if not title:
            print("Title cannot be empty.")
        else:
            self.artworks.append(title)
            print(f"'{title}' added.")

    def remove_artwork(self, title):
        # TODO 3
        if title in self.artworks:
            self.artworks.remove(title)
            print(f"'{title}' removed.")
        else:
            print(f"'{title}' is not in the gallery.")

    def show(self):  # (given) A
        print(f"{self.gallery_name}, artworks: {len(self.artworks)}", self.artworks)

    # TODO 4
    def __del__(self):
        print(f"Closing {self.gallery_name}. Goodbye!")


gallery = ArtGallery("Little Brushes Gallery", "Portland")  # (given) B

while True:  # (given) C: menu
    choice = input("\n1. Add  2. Remove  3. Show  4. Close\nChoice: ").strip()

    if choice == "1":
        gallery.add_artwork(input("Title: ").strip())
    elif choice == "2":
        gallery.remove_artwork(input("Title to remove: ").strip())
    elif choice == "3":
        gallery.show()
    elif choice == "4":
        del gallery
        break
    else:
        print("Please type 1, 2, 3 or 4.")