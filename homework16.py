import random
text_data = input('Write your text: ').split()
text_data_index = []
for i in range(len(text_data)):
    text_data_index.append(text_data[i] + '_' + str(i+1))

shuffled_data_index = []
while text_data_index != []:
    word = random.choice(text_data_index)
    shuffled_data_index.append(word)
    text_data_index.remove(word)

secret_indexes = []
for i in range(len(shuffled_data_index)):
    index = shuffled_data_index[i].split('_')[-1]  # index in str
    index = int(index)  # index in digit
    secret_indexes.append(index)
    shuffled_data_index[i] = '_'.join(shuffled_data_index[i].split('_')[:-1])

print(shuffled_data_index)
print(secret_indexes)
a = open('homework16.1.txt' , 'w')
b = open('homework16.2.txt' , 'w')
a.write(str(secret_indexes))
b.write(str(shuffled_data_index))
        
        
    
    
