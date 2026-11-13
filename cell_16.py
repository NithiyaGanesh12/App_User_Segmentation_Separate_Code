# Save outputs and model
df.to_csv(OUT/'users_with_clusters.csv',index=False)
profiles.to_csv(OUT/'cluster_profiles.csv')
centers.to_csv(OUT/'standardized_cluster_centers.csv')
pca_df.to_csv(OUT/'pca_coordinates.csv',index=False)
pd.DataFrame(stability).to_csv(OUT/'seed_stability.csv',index=False)
for c in profiles.index:
    df.loc[df.cluster_id==c,['user_id','cluster_id','segment']].to_csv(OUT/f'cluster_{c}_users.csv',index=False)
joblib.dump({'features':FEATURES,'preprocessor':prep,'model':model,'segment_names':names},OUT/'segmentation_model.joblib')
summary={'source':'SYNTHETIC DEMONSTRATION' if DATA_PATH is None else str(DATA_PATH),'users':len(df),'selected_k':selected,'silhouette_best_k':best,**evaluation.set_index('k').loc[selected].to_dict(),'pca_2d_variance':float(pca.explained_variance_ratio_.sum()),'seed_stability':stability}
(OUT/'run_summary.json').write_text(json.dumps(summary,indent=2))
(OUT/'project_report.txt').write_text(json.dumps(summary,indent=2)+'\n\n'+profiles.round(3).to_string()+'\n\nSynthetic results are not actual-dataset findings. Engagement is not a churn probability or monetary value. PCA is visualization only.')
print(json.dumps(summary,indent=2))
