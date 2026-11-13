# Elbow and silhouette plots
fig,axes=plt.subplots(1,2,figsize=(13,5))
axes[0].plot(evaluation.k,evaluation.inertia,'o-'); axes[0].set(title='Elbow diagnostic',xlabel='k',ylabel='Inertia')
axes[1].plot(evaluation.k,evaluation.silhouette,'o-'); axes[1].axvline(selected,color='red',ls='--'); axes[1].set(title='Sampled silhouette',xlabel='k')
fig.tight_layout(); fig.savefig(OUT/'cluster_selection.png'); plt.show()
