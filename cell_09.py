# Evaluate candidate cluster counts
models={}; rows=[]
with threadpool_limits(limits=2):
    for k in range(2,9):
        m=KMeans(n_clusters=k,n_init=10,random_state=42).fit(Z)
        models[k]=m
        rows.append({'k':k,'inertia':m.inertia_,'silhouette':silhouette_score(Z,m.labels_,sample_size=min(1500,len(Z)),random_state=42),'davies_bouldin':davies_bouldin_score(Z,m.labels_),'calinski_harabasz':calinski_harabasz_score(Z,m.labels_)})
evaluation=pd.DataFrame(rows)
evaluation.to_csv(OUT/'cluster_evaluation.csv',index=False)
display(evaluation)
