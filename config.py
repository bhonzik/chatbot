import os

### 

###############
### FOLDERS ###
###############

root_folder = "data"

input_folder = os.path.join(root_folder, "input")

token_folder = os.path.join(root_folder, "tokenized")

dictionary_file = os.path.join(root_folder, "dictionary.txt")

dictionarized_folder = os.path.join(root_folder, "dict_sequence")

chunk_folder = os.path.join(root_folder, "chunks")

tensor_folder = os.path.join(root_folder, "tensors")