from ArchiveItems import *

def save_to_file(items, fileName):
    with open(fileName, 'w') as file:
        for i in items:
            if i.uid.startswith("B"):
                file.write(f"Book,{i.uid},{i.title},{i.year},{i.author},{i.pages}\n")
            elif i.uid.startswith("A"):
                file.write(f"Article,{i.uid},{i.title},{i.year},{i.journal},{i.doi}\n")
            elif i.uid.startswith("P"):
                file.write(f"Podcast,{i.uid},{i.title},{i.year},{i.host},{i.duration}\n")

def load_from_file(fileName):
    items = list()
    with open(fileName) as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(",")
            if parts[0] == "Book":
                items.append(Book(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
            elif parts[0] == "Article":
                items.append(Article(parts[1], parts[2], int(parts[3]), parts[4], parts[5]))
            elif parts[0] == "Podcast":
                items.append(Podcast(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
    return items

def main():

    book1 = Book("B001", "Title3", 2021, "Author1", 100)
    book2 = Book("B002", "Title4", 2021, "Author2", 300)
    article1 = Article("A001", "Title5", 2017, "Journal1", "11.5432")
    article2 = Article("A002", "Title6", 2017, "Journal2", "10.1234")
    podcast1 = Podcast("P001", "Title7", 2012, "Host1", 60)
    podcast2 = Podcast("P002", "Title8", 2012, "Host2", 180)
    
    items = [book1, book2, article1, article2, podcast1, podcast2]
    save_to_file(items, "archive.txt")
    items.clear()
    items = load_from_file("archive.txt")
    
    print("Print everything inside the items:")
    for i in items:
        if i.uid.startswith("B"):
            print("Book -> " + str(i))
        elif i.uid.startswith("A"):
            print("Article -> " + str(i))
        elif i.uid.startswith("P"):
            print("Podcast -> " + str(i))
    
    print("\nRecent Items:")
    for i in items:
        if i.is_recent(5):
            print(i)
    
    print("\nArticle with DOI starting '10.1234':")
    for i in items:
        if i.uid.startswith("A") and i.doi.startswith("10.1234"):
            print(i)
    
if __name__ == "__main__":
    main()