# Correlation heatmap
fig,ax=plt.subplots(figsize=(10,7))
sns.heatmap(X.corr(),annot=True,cmap='coolwarm',center=0,ax=ax)
fig.tight_layout(); fig.savefig(OUT/'eda_correlation.png'); plt.show()
