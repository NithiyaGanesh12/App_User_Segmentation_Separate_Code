# Cluster centers and sizes
fig,ax=plt.subplots(figsize=(11,6))
sns.heatmap(centers,annot=True,center=0,cmap='vlag',ax=ax)
fig.tight_layout(); fig.savefig(OUT/'cluster_centers_heatmap.png'); plt.show()
fig,ax=plt.subplots(figsize=(9,5))
ax.bar(profiles.index.astype(str),profiles.users)
ax.set(title='Users per cluster',xlabel='Cluster ID',ylabel='Users')
fig.tight_layout(); fig.savefig(OUT/'cluster_sizes.png'); plt.show()
