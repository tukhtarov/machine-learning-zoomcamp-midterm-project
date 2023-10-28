import pandas as pd
import pickle
from scipy.io.arff import loadarff 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

raw_data = loadarff('phpkIxskf.arff')
df = pd.DataFrame(raw_data[0])

df.columns = df.columns.str.lower()
df = df.rename(columns={
    "v1": "age",
    "v2": "job",
    "v3": "marital_status",
    "v4": "education",
    "v5": "credit_in_default",
    "v6": "average_balance",
    "v7": "has_housing_loan",
    "v8": "has_personal_loan",
    "v9": "contact_type",
    "v10": "day",
    "v11": "month",
    "v12": "duration",
    "v13": "number_contacts",
    "v14": "pdays",
    "v15": "number_contacts_before",
    "v16": "previous_outcome",
    "class": "target"})

for feat in ['job', 'marital_status', 'education', 'credit_in_default', 'has_housing_loan', 'has_personal_loan', 'contact_type', 'month', 'previous_outcome', 'target']:
    df[feat] = df[feat].str.decode('utf-8')

df['target'] = (df['target'] == '2').astype(int)   

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

y_full_train = df_full_train.target.values
del df_full_train['target']

y_test = df_test['target'].values
del df_test['target']

dv = DictVectorizer(sparse=False)

full_train_dict = df_full_train.to_dict(orient='records')
X_full_train = dv.fit_transform(full_train_dict)

test_dict = df_test.to_dict(orient='records')
X_test = dv.fit_transform(test_dict)

print('Training the model...')

model = LogisticRegression(max_iter=5000, C=0.1)
model.fit(X_full_train, y_full_train)
y_pred = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_pred)

print('auc:', auc)

output_file = 'model.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'The model is saved to {output_file}')    