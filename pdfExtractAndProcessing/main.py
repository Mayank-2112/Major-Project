#import dependencies..
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')

#extracting text from PDF file 1

from pdfminer.high_level import extract_text

text1 = extract_text('pdfExtractAndProcessing\Resume_Updated.pdf')
# print(text1)

#extracting text from PDF file 2

# text2 = extract_text('pdfExtractAndProcessing\Mohit_kumar.pdf')
# print(text2)



#tokenization from file 1

from nltk.tokenize import word_tokenize

words1 = word_tokenize(text1)
# print(len(words1))
# print(words1)
cleaned_tokens1 = [re.sub(r'[^\w\s]', '', i) for i in words1 if re.sub(r'[^\w\s]', '', i)]
# print(cleaned_tokens1)
# print(len(cleaned_tokens1))

#tokenization from file 2

# words2 = word_tokenize(text2)
# print(len(words1))
# print(words1)
# cleaned_tokens2 = [re.sub(r'[^\w\s]', '', i) for i in words2 if re.sub(r'[^\w\s]', '', i)]
# print(cleaned_tokens2)
# print(len(cleaned_tokens2))


#Removing stop words1

from nltk.corpus import stopwords

stop_words1 = set(stopwords.words('english'))

filtered_words1 = []
for i in cleaned_tokens1:
    if i not in stop_words1:
        filtered_words1.append(i)

print(filtered_words1)
# print(len(filtered_words1))

# stop_words2 = set(stopwords.words('english'))

# filtered_words1 = []
# for i in cleaned_tokens1:
#     if i not in stop_words1:
#         filtered_words1.append(i)

# print(filtered_words1)
# print(len(filtered_words1))



#Removing Duplicate words1

final_words1 = set(filtered_words1)

print(final_words1)
print(len(final_words1))
