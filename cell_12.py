# Profiles and segment names
imputed=pd.DataFrame(prep.named_steps['imputer'].transform(X),columns=FEATURES)
imputed['cluster_id']=model.labels_
profiles=imputed.groupby('cluster_id')[FEATURES].mean()
profiles['users']=df.groupby('cluster_id').size()
profiles['percentage']=profiles.users/len(df)*100
centers=pd.DataFrame(model.cluster_centers_,columns=FEATURES)
engagement=centers.mul([1,1,1,1,-1],axis=1).mean(axis=1)
order=engagement.sort_values().index.tolist()
names={c:f'Engagement tier {i+1} of {selected}' for i,c in enumerate(order)}
names[order[0]]='Low engagement - review retention'
names[order[-1]]='High engagement'
df['segment']=df.cluster_id.map(names)
profiles['segment']=profiles.index.map(names)
profiles['engagement_index']=engagement
profiles['suggested_action']=['Test reactivation and review onboarding' if c==order[0] else 'Test loyalty and advanced features' if c==order[-1] else 'Test relevant feature education' for c in profiles.index]
display(profiles)
