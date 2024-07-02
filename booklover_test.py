import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        '''
        add a book and test if it is in `book_list`.
        '''
        booklover1 = BookLover('user1','user1@gmail.com','sci-fi')
        booklover1.add_book('Dune', 4)
        
        expected = 'Dune' in booklover1.book_list.book_name.to_list()
        self.assertTrue(expected)

    def test_2_add_book(self):
        '''
        add the same book twice. Test if it's in `book_list` only once.
        '''
        booklover2 = BookLover('user2','user2@gmail.com','fiction')
        booklover2.add_book('Moby Dick', 3)
        booklover2.add_book('Moby Dick', 4)
        
        count = booklover2.book_list.book_name.value_counts()['Moby Dick']
        expected = 1
        self.assertEqual(count, expected)
                
    def test_3_has_read(self):
        '''
        pass a book in the list and test if the answer is `True`.
        '''
        booklover3 = BookLover('user3','user3@gmail.com','romance')
        booklover3.add_book('Pride and Prejudice', 5)
        
        testValue = booklover3.has_read('Pride and Prejudice')
        
        self.assertTrue(testValue)
        
    def test_4_has_read(self): 
        '''
        pass a book NOT in the list and use `assert False` to 
        test if the answer is `True`
        '''
        booklover4 = BookLover('user4','user4@gmail.com','mystery')
        booklover4.add_book('Sherlock Holmes', 3)
        
        testValue = booklover4.has_read('Nancy Drew')
        self.assertFalse(testValue)
        
    def test_5_num_books_read(self): 
        '''
        add some books to the list, and test num_books matches expected.
        '''
        booklover5 = BookLover('user5','user5@gmail.com','fantasy')
        booklover5.add_book('The Wizard of Oz', 5)
        booklover5.add_book('Ozma of Oz', 4)
        
        count = booklover5.num_books_read()
        expected = 2
        self.assertEqual(count, expected)

    def test_6_fav_books(self):
        '''
        add some books with ratings to the list, making sure some 
        of them have rating > 3. 
        Test checks that the returned books have rating  > 3
        '''
        booklover6 = BookLover('user6','user6@gmail.com','non fiction')
        booklover6.add_book('Walden', 2)
        booklover6.add_book('The Republic', 5)
        
        testValue = (booklover6.fav_books().book_rating > 3).all()
        self.assertTrue(testValue)
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
    
    
