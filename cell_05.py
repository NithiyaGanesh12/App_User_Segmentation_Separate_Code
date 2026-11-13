# Validate users and clean features
required=['user_id']+FEATURES
missing=set(required)-set(raw.columns)
if missing: raise ValueError(f'Missing columns: {sorted(missing)}')
df=raw.drop_duplicates().reset_index(drop=True).copy()
df.user_id=df.user_id.astype('string').str.strip()
if df.user_id.isna().any() or df.user_id.eq('').any() or df.user_id.duplicated().any():
    raise ValueError('Require one row per unique nonmissing user_id')
def clean_features(data):
    x=data[FEATURES].apply(pd.to_numeric,errors='coerce').replace([np.inf,-np.inf],np.nan)
    x=x.mask(x<0)
    x.loc[x.active_days_30>30,'active_days_30']=np.nan
    return x
X=clean_features(df)
if len(X)<20 or X.isna().all().any(): raise ValueError('Insufficient users or entirely missing feature')
quality={'synthetic_demo':DATA_PATH is None,'users':len(df),'duplicates_removed':len(raw)-len(df),'missing_after_cleaning':X.isna().sum().to_dict()}
(OUT/'data_quality.json').write_text(json.dumps(quality,indent=2))
display(X.describe())
