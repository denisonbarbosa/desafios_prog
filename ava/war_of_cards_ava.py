from queue import SimpleQueue

def war_of_cards():
    
    library_1 = SimpleQueue()
    library_2 = SimpleQueue()

    print(library_1.qsize(), library_1.empty())
    print(library_2.qsize(), library_2.empty())

    pass

if __name__ == '__main__':
    war_of_cards()