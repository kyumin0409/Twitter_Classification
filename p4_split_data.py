#Input Paths
data_path = './app_data/brexit/brexit_data2.txt'
label_path = './app_data/brexit/brexit_labels.txt'

#Output Paths
train_data_path = './app_data/brexit/brexit_train_data.txt'
train_labels_path = './app_data/brexit/brexit_train_labels.txt'
test_data_path = './app_data/brexit/brexit_test_data.txt'
test_labels_path = './app_data/brexit/brexit_test_labels.txt'

#Read data/labels and determine training split
with open(data_path, "r",  encoding="utf-8") as f:
    data = f.readlines()
with open(label_path, "r",  encoding="utf-8") as f:
    labels = f.readlines()
assert(len(data) == len(labels))
split_point = int(len(data)*.75)

#Split test/training on data
train_data = data[0:split_point]
test_data = data[split_point+1:]
with open(train_data_path, "w+",  encoding="utf-8") as f:
    f.writelines(train_data)
with open(test_data_path, "w+",  encoding="utf-8") as f:
    f.writelines(test_data)

#Split test/training on labels
train_labels = labels[0:split_point]
test_labels = labels[split_point+1:]
with open(train_labels_path, "w+",  encoding="utf-8") as f:
    f.writelines(train_labels)
with open(test_labels_path, "w+",  encoding="utf-8") as f:
    f.writelines(test_labels)