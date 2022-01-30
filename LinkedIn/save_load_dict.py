'''
The goal here is to save a dictionary in a file, to load it later!
We use the module pickle! 
test_dict.pickle is a binary file!
'''
import pickle

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)
    
def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

test_dict = {1: 'a', 2: 'b', 3: 'c'}
save_dict(test_dict, 'test_dict.pickle')
recovered = load_dict('test_dict.pickle')
print(recovered)