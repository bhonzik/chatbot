import config
import ast
import tensorflow as tf
from keras._tf_keras.keras.layers import Embedding, LSTM, Dense

# Copy already-existing dictionary as "text"
with open(config.dictionary_file, "r") as f:
    text = f.read()

# Initialize dictionary as a Python dictionary
dictionary = ast.literal_eval(text)

# Calculate vocabulary size
vocab_size = len(dictionary)

class JonesGPT(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, **kwargs):
        
        super().__init__(**kwargs)

        self.embedding = Embedding(
            input_dim = vocab_size,
            output_dim = embedding_dim
        )

        self.lstm1 = LSTM(128)
        self.lstm2 = LSTM(64)
        self.dense1 = Dense(32, activation="relu")
        self.dense = Dense(vocab_size, activation="softmax")
    
    def call(self, inputs):
        x = self.embedding(inputs)
        x = self.lstm1(x)
        x = self.lstm2(x)
        x = self.dense1(x)
        return self.dense2(x)
    
model = JonesGPT(vocab_size, config.embedding_dim)