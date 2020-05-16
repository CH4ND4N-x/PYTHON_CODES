#code challenge 2
class Book:
    def __init__(self,authorlast,authorfirst,title,place,publisher,year):
        self.authorfirst=authorfirst
        self.authorlast=authorlast
        self.title=title
        self.place=place
        self.publisher=publisher
        self.year=year
    def write_bib_entry(self):
        return self.authorlast+","+self.authorfirst+","+self.title+","+self.place+","+self.publisher,self.year
    def change(self,year):
        self.year=year
    def make_authoryear(self):
        authoryear=self.authorlast+"("+str(self.year)+")"
        print(authoryear)
"""1.Create a two instances of Book in the name of beauty and pynut
        The Evidential Power of Beauty
        Python in a Nutshell"""    

beauty=Book("Dubay","Thomes","The Evidential Power of Beauty","USA","Ignatius Press",1999) 
pynut=Book("Martelli","Alex","Python in a Nutshell","Sebastopol, CA","O'Reilly Media, Inc.",2003)   


"""2.print beauty.write_bib_entry() at the interpreter, what will happen"""
print(beauty.write_bib_entry())
print(pynut.write_bib_entry())


"""3.print out the author attribute of the pynut instance"""
print(pynut.authorfirst,pynut.authorlast)


"""4.change the publication year for the beauty book to"2010"""
beauty.change(2010)
print(beauty.write_bib_entry())



