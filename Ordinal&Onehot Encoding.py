import pandas as pd

file_path = 'data.csv'
data = pd.read_csv(file_path)

cat_columns = data.select_dtypes(include=['object']).columns.tolist()


ordinal_columns = ['size']
onehot_columns = [col for col in cat_columns if col not in ordinal_columns]

ordinal_mappings = {
    'Size': {'S': 0, 'M': 1, 'L': 2}
}

for col in ordinal_columns:
    if col in ordinal_mappings:
        data[col + '_encoding'] = data[col].map(ordinal_mappings[col])

for col in onehot_columns:
    onehot_data = pd.get_dummies(data[col], prefix=col)
    data = data.join(onehot_data).drop(col, axis=1)

data.to_csv('new_data.csv', index=False)

print(data)
