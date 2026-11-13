# Imputation and scaling
prep=Pipeline([('imputer',SimpleImputer(strategy='median')),('scaler',StandardScaler())])
Z=prep.fit_transform(X)
if len(np.unique(Z,axis=0))<9: raise ValueError('Need at least 9 distinct behavioral records')
display(pd.DataFrame(Z,columns=FEATURES).head())
