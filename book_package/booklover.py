import pandas as pd

# Task 1
class BookLover():
    
    def __init__(self,
                 name, 
                 email, 
                 fav_genre, 
                 num_books = 0, 
                 book_list =  pd.DataFrame(
                     {'book_name':[], 
                      'book_rating':[]}
                 )):
        '''
        initializing attributes
        '''
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name, rating):
        '''
        This function takes a book name (string) and 
        rating (integer from 0 to 5)
        '''
        if book_name not in self.book_list.book_name.to_list():
            new_book = pd.DataFrame({'book_name': [book_name],
                                     'book_rating':[rating]})
            self.book_list = pd.concat([self.book_list, new_book], 
                                       ignore_index=True)
    
    def has_read(self, book_name):
        '''
        This function takes book_name (string) as input and determines 
        if the person has read the book
        '''
        return book_name in self.book_list.book_name.to_list()
    
    def num_books_read(self):
        '''
        This function takes no parameters and just returns the total 
        number of books the person has read.
        '''
        return len(self.book_list)
    
    def fav_books(self):
        '''
        This function takes no parameters and returns the filtered 
        dataframe of the person’s most favorite books.
        '''
        top_books = self.book_list[self.book_list.book_rating > 3]
        return top_books.sort_values('book_rating',
                                              ascending = False)

    
    
