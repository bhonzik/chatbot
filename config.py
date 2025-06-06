import os

##################
### PARAMETERS ###
##################

# Length of each input sequence
sequence_length = 6

# Number of generated X_train/Y_train tensor pairs for
# each token
sample_rate = 0.1

# Number of dimensions for token embedding
embedding_dim = 50

###############
### FOLDERS ###
###############

root_folder = "data"

input_folder = os.path.join(root_folder, "input")

token_folder = os.path.join(root_folder, "tokenized")

dictionary_file = os.path.join(root_folder, "dictionary.txt")

dictionarized_folder = os.path.join(root_folder, "dict_sequence")

tensor_folder = os.path.join(root_folder, "tensors")