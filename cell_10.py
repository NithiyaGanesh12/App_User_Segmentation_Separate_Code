# Select a model
REQUESTED_K=None  # Set to 4 for an explicit four-cluster comparison.
best=int(evaluation.loc[evaluation.silhouette.idxmax(),'k'])
selected=best if REQUESTED_K is None else REQUESTED_K
if selected not in models: raise ValueError('k must be 2..8')
model=models[selected]
df['cluster_id']=model.labels_
print('Selected k:',selected)
