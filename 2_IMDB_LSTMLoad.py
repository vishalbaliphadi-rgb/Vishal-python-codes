#################################################################################
# Step-1 Import required libraries
################################################################################

from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,LSTM , Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences

####################################################################
# Step-2 Configuration of Values
####################################################################

VOCAB_SIZE = 10000 # Consider most frequent 10000 unique words
MAX_LENGTH = 200   # Consider max 200 words in review

#####################################################################
# Step-3 Load the IMDB dataset (Internation Movie Database)
#####################################################################

print ("-"*40)
print ("Movie Review Sentiment Analysis Using LSTM")
print ("-"*40)

print ("Loding the Dataset...")

(X_train, Y_train), (X_test, Y_test) = imdb.load_data (num_words = VOCAB_SIZE)

print ("IMDB dataset loaded succesfully")

print ("Number of training reviews: ", len(X_train))
print ("Number of testing reviews: ", len(X_test))

#########################################################################
# X_train - Reviews used for training
# Y_train - Actual Sentiments of training
# X_test  - Reviwes used for testing
# Y_test  - Actual sentiments of testing

# Sentiment :
# 0 - Negative sentiment
# 1 - Positive Sentiment
##########################################################################

##########################################################################
# Step - 4   Load the word Dictionary
#########################################################################

word_index = imdb.get_word_index()

# Dictionary contains mapping of word and it's corresponding number
# Drisham is good movie  --> (20 56 78 43)
# for example 20 - Drisham, 56- is , 78- good, 43- movie

##############################################################################
# Step-5 Create reverse dictionary
##############################################################################

reverse_word_index = {}

for word,index in word_index.items():
    reverse_word_index[index+3] = word


#########################################################################
# Step-6 Function to decode the review (Number to word)
######################################################################

def DecodeReivew(encoded_review):
    words =[]

    for number in encoded_review:
        if number >= 3: # ignore first 3
            word = reverse_word_index.get(number,"?")
            words.append(word)

    return" ".join(words)  # Join the list of words


############################################################################
# Step-7 - Display Sample reviews
##############################################################################

print ("-"*40)
print ("------------------Sample Reviews----------------------------")
print ("-"*40)

for i in range(3,7):
    review = DecodeReivew(X_train[i])

    print ("-"*40)

    print ("Review number: ", i+1)
    print ("Review: ")
    print (review)

    print ("-"*40)

    if Y_train[i] == 1:
        print ("Sentiment: Positive")
    else:
        print ("Sentiment: Negative")

#####################################################################################
# Step-8 Padding
######################################################################################

X_train_padded = pad_sequences(
    X_train,
    maxlen = MAX_LENGTH
)

print ("Padded trained data:\n ", X_train_padded.shape)

X_test_padded = pad_sequences( 
    X_test,
    maxlen = MAX_LENGTH
)

print ("Padded tested data:\n ", X_test_padded.shape)

########################################################################################
# Step-9 Create LSTM Model
#######################################################################################

model = Sequential()

model.add(
    Embedding(
        input_dim=VOCAB_SIZE,
        output_dim=32,  # each word is represented in 32 values

    )
)

model.add(
    LSTM(
        units = 64 # Size of LSTM hidden state
    )
)

model.add (
    Dense (
        units=1,    # one output
        activation="sigmoid"  # Used to produce probability
    )
)

# Project Architecture
# Review ---> Embedding ---> LSTM ----> Dense ----> Sigmoid ---> Positive/Negative


####################################################################################
# Step-10 - Compile the model
####################################################################################

model.compile (
    optimizer = "adam" ,             # Algorithm to update weights
    loss = "binary_crossentropy",    # Loss function
    metrics = ["accuracy"]           # measure classification accuracy
)

print ("Model compiled successfully")

######################################################################################
# Step-11 - Train the model
#######################################################################################

print ("Model training")

model.fit (
    X_train_padded,         # Input training reviews
    Y_train,                # Actual Sentiment labels
    epochs = 3,             # Complete dataset gets processesd 3 times
    batch_size = 64,        # Process 64 reviews in one batch
    validation_split = 0.2  # Use 20% training data for validation

       
)

print ("Model training gets completed")

######################################################################################
# Step-12: Evaluate the model
######################################################################################

accuracy = model.evaluate (
    X_test_padded,          # Testing reviews
    Y_test ,                 # Actual Testing labels
    verbose = 0             # Dont display the proceess bar
)

print ("Testing Accuracy: ", accuracy)

######################################################################################
# Step-13: Predict the review
#########################################################################################

TEST_REVIEW_NUMBER = 0

original_review = X_test[TEST_REVIEW_NUMBER]

decoded_review = DecodeReivew(original_review)

print ("Review given to the model: ")
print (decoded_review)

##################################################################################
# Step-14: Get the actual sentiment
###################################################################################

actual_value = Y_test[TEST_REVIEW_NUMBER]

if actual_value == 1:
    actual_sentiment = "POSITIVE"
else:
    actual_sentiment = "NEGATIVE"

print ("Actual Sentiment: ", actual_sentiment)

####################################################################################
# Step-15: Predict the sentiment
####################################################################################

review_for_prediction = X_test_padded[TEST_REVIEW_NUMBER: TEST_REVIEW_NUMBER+1]

prediction = model.predict(
    review_for_prediction,
    verbose = 0
)

probability = prediction[0][0]

if probability >=0.5:
    predicted_sentiment = "Positive"
else:
    predicted_sentiment = "Negative"

print ("Final Result")
print ("Prediction Probability: ", probability)
print ("Actual Sentiment: ",actual_sentiment)
print ("Predicted Sentiment: ", predicted_sentiment)

print ("-"*40)