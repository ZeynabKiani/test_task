# Feature extraction from 'CreatedAt'
X_train['Created_at'] = pd.to_datetime(X_train['Created_at'])
X_test['Created_at'] = pd.to_datetime(X_test['Created_at'])

X_train['Month'] = X_train['Created_at'].dt.month
X_train['Day'] = X_train['Created_at'].dt.day
X_train['Hour'] = X_train['Created_at'].dt.hour

X_test['Month'] = X_test['Created_at'].dt.month
X_test['Day'] = X_test['Created_at'].dt.day
X_test['Hour'] = X_test['Created_at'].dt.hour

X_train = X_train.drop('Created_at', axis=1)
X_test = X_test.drop('Created_at', axis=1)
