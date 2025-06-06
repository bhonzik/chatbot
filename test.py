from main import * # This allows us to access all of the
                   # functions and variables within main.py
                   # without needing to specify the source;
                   # for example, "main.tokenize_files" or
                   # "main.config.token_folder"

tokenize_files(config.input_folder,
               config.token_folder)
generate_dictionary(config.token_folder,
                    config.dictionary_file)
dictionarize_files(config.token_folder,
                   config.dictionarized_folder)
tensorize_files(config.dictionarized_folder,
                config.tensor_folder,
                config.sample_rate,
                config.sequence_length)