# Aggregation Example
# If we want to change association level
# from aggregation to composition, all we
# have to do is pass arguments of the content 
# class to the container class and create 
# objects in the __init__() method.
# e.g. pass the text to SubChapter and create
# Paragraph (content) inside the __init__() 
# method of the SubChapter (container) class.
# By doing so the Paragraph instance will become
# dependent to SubChapter instance's lifespan.

class Paragraph:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class SubChapter:
    def __init__(self, title, paragraphs=[]):
        self.title = title
        self.paragraphs = paragraphs

    def __str__(self):
        s = f'### {self.title}\n'
        for x in self.paragraphs:
            s += x + '\n'
        return s


class Chapter:
    def __init__(self, title, sub_chapters=[]):
        self.title = title
        self.sub_chapters = sub_chapters

    def __str__(self):
        s = f'## {self.title}\n'
        for x in self.sub_chapters:
            s += x.__str__()
        return s


class Book:
    def __init__(self, title, year, ISBN, chapters=[], authors=[]):
        self.title = title
        self.year = year
        self.ISBN = ISBN
        self.chapters = chapters
        self.authors = authors

    def __str__(self):
        authors = ', '.join([a.full_name for a in self.authors])
        s = f'# {self.title}\n'
        s += f'*by {authors} in {self.year}*\n'
        for x in self.chapters:
            s += x.__str__()
        s += '\n'
        s += f'ISBN: {self.ISBN}'
        return s


class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + ' ' + last_name

    def __str__(self):
        return self.full_name


authors = [Author('Dusty', 'Phillips'), Author(
    'Chetan', 'Giridhar'), Author('Sakis', 'Kasampalis')]


paragraphs = []
paragraphs.append(
    '''
    Everyone knows what an object is—a tangible thing that we can sense, feel,
    and manipulate. The earliest objects we interact with are typically baby toys.
    Wooden blocks, plastic shapes, and over-sized puzzle pieces are common first
    objects. Babies learn quickly that certain objects do certain things: bells ring,
    buttons press, and levers pull.
    '''
)
paragraphs.append(
    '''
    The definition of an object in software development is not terribly different. Software
    objects are not typically tangible things that you can pick up, sense, or feel, but they
    are models of something that can do certain things and have certain things done to
    them. Formally, an object is a collection of data and associated behaviors.
    '''
)
paragraphs.append(
    '''
    So, knowing what an object is, what does it mean to be object-oriented? Oriented
    simply means directed toward. So object-oriented means functionally directed towards
    modeling objects. This is one of the many techniques used for modeling complex
    systems by describing a collection of interacting objects via their data and behavior.
    '''
)

sub_chapter = SubChapter('Introducing object-oriented', paragraphs)
chapter = Chapter('Object-oriented Design', [sub_chapter])
book = Book('Python: Master the Art of Design Patterns',
            2016, '978-1-78712-518-6', [chapter], authors)

print(book)
