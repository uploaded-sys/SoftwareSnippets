class Book:
    def __init__(self, title, author, publication_year, magical_level):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.magical_level = magical_level

    def display_info(self):
        print(self.title)
        print(self.author)
        print(self.publication_year)
        print(self.magical_level)

    def is_rare(self):
        statement = "magic state:"
        if self.magical_level > 8:
            print(statement,"is truly rare")
        else:
            print(statement,"is not rare")

    def update_magical_level(self, new_level):
        self.magical_level = new_level

    def age_of_book(self, current_year):
        return current_year - self.publication_year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}, Magical Level: {self.magical_level}"
