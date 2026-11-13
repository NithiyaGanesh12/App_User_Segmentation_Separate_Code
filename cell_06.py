# EDA distributions
X.describe().to_csv(OUT/'eda_summary.csv')
fig,axes=plt.subplots(2,3,figsize=(14,8))
for ax,c in zip(axes.flat,FEATURES):
    ax.hist(X[c].dropna(),bins=35); ax.set_title(c)
axes.flat[-1].axis('off')
fig.tight_layout(); fig.savefig(OUT/'eda_distributions.png'); plt.show()
