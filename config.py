import os

##################
### PARAMETERS ###
##################

# Length of each dictionarized chunk for pre-processing
chunk_length = 6

# Amount of chunks within the program's context window
memory_length = 2

# Number of generated X_train/Y_train tensor pairs for
# each chunk
sample_rate = 0.5

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