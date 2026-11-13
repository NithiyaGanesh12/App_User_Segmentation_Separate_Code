# Seed stability
stability=[]
with threadpool_limits(limits=2):
    for seed in [7,21,99]:
        alternative=KMeans(n_clusters=selected,n_init=10,random_state=seed).fit_predict(Z)
        stability.append({'seed':seed,'ARI':adjusted_rand_score(model.labels_,alternative)})
display(pd.DataFrame(stability))
