class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year
    
    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"
    
    def __eq__(self, other):
        return self.uid == other.uid
    
    def is_recent(self, n):
        return self.year >= (2025 - n)

class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        ArchiveItem.__init__(self, uid, title, year)
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}, Author: {self.author}, Pages: {self.pages}"

class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        ArchiveItem.__init__(self, uid, title, year)
        self.journal = journal
        self.doi = doi
    
    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}, Journal: {self.journal}, DOI: {self.doi}"

class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        ArchiveItem.__init__(self, uid, title, year)
        self.host = host
        self.duration = duration
    
    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}, Host: {self.host}, DUration: {self.duration}"

def main():
    arcItem1 = ArchiveItem("A001", "Title1", 2024)
    arcItem2 = ArchiveItem("A002", "Title2", 2024)
    book1 = Book("B001", "Title3", 2021, "Author1", 100)
    book2 = Book("B002", "Title4", 2021, "Author2", 300)
    article1 = Article("AR001", "Title5", 2017, "Journal1", "DOI1")
    article2 = Article("AR002", "Title6", 2017, "Journal2", "DOI2")
    podcast1 = Podcast("P001", "Title7", 2012, "Host1", 60)
    podcast2 = Podcast("P002", "Title8", 2012, "Host2", 180)

    items = [arcItem1, arcItem2, book1, book2, article1, article2, podcast1, podcast2]

    for i in items:
        print(i)

if __name__ == "__main__":
    main()