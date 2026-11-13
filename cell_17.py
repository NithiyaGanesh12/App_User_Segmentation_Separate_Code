# New-user prediction
def predict_new_users(data,model_path):
    bundle=joblib.load(model_path)  # Trusted model files only.
    if bundle['features']!=FEATURES: raise ValueError('Feature configuration mismatch')
    result=data.rename(columns=COLUMN_MAPPING).copy()
    scaled=bundle['preprocessor'].transform(clean_features(result))
    result['cluster_id']=bundle['model'].predict(scaled)
    result['segment']=result.cluster_id.map(bundle['segment_names'])
    return result
new_users=pd.DataFrame({'user_id':['NEW_001','NEW_002'],'sessions_per_week':[24,2],'avg_session_minutes':[30,5],'active_days_30':[25,3],'features_used':[10,2],'days_since_last_login':[1,24]})
predictions=predict_new_users(new_users,OUT/'segmentation_model.joblib')
predictions.to_csv(OUT/'new_user_predictions.csv',index=False)
display(predictions)
