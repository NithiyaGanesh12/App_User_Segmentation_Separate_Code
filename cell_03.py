# Synthetic demonstration generator
def demo_data(n=50000):
    rng=np.random.default_rng(42)
    groups=rng.choice(4,n,p=[.25,.35,.25,.15])
    centers=np.array([[26,32,26,11,1],[12,17,17,7,4],[2,4,3,2,23],[4,26,6,5,10]])
    x=np.maximum(centers[groups]+rng.normal(size=(n,5))*[2.5,3,2,1,1.8],0)
    x[:,2]=np.clip(np.round(x[:,2]),0,30)
    x[:,3]=np.round(x[:,3])
    result=pd.DataFrame(x,columns=FEATURES)
    result.insert(0,'user_id',[f'USER_{i:06d}' for i in range(n)])
    for c in FEATURES:
        result.loc[rng.choice(n,int(n*.01),replace=False),c]=np.nan
    return pd.concat([result,result.iloc[:50]],ignore_index=True)
