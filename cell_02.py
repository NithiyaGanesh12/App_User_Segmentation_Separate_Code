# Imports and configuration
from pathlib import Path
import json, joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score, adjusted_rand_score
from threadpoolctl import threadpool_limits
DATA_PATH = None  # Replace with your CSV filename for actual data.
COLUMN_MAPPING = {}
FEATURES = ['sessions_per_week','avg_session_minutes','active_days_30','features_used','days_since_last_login']
OUT = Path('demo_results' if DATA_PATH is None else 'actual_results')
OUT.mkdir(exist_ok=True, parents=True)
