import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

class PCAProcessor:
    def __init__(self, n_components=0.9, scale=True):
        self.n_components = n_components
        self.scale = scale
        self.scaler = None
        self.pca = None
        self.feature_names = None

    def fit_transform(self, df, exclude_cols=None):
        if exclude_cols is None:
            exclude_cols = ["season", "team_name"]

        df = df.reset_index(drop=True)

        numeric_df = df.select_dtypes(include=["number"]).drop(
            columns=[col for col in exclude_cols if col in df.columns], errors="ignore"
        )

        self.feature_names = numeric_df.columns.tolist()

        X = numeric_df.to_numpy()
        if self.scale:
            self.scaler = StandardScaler()
            X = self.scaler.fit_transform(X)

        self.pca = PCA(n_components=self.n_components)
        X_pca = self.pca.fit_transform(X)

        pca_cols = [f"PC{i+1}" for i in range(X_pca.shape[1])]
        df_pca = pd.DataFrame(X_pca, columns=pca_cols)

        identifiers = df[exclude_cols].reset_index(drop=True)
        df_final = pd.concat([identifiers, df_pca], axis=1)

        return df_final

    def explained_variance(self):
        if self.pca is None:
            raise ValueError("PCA not fitted yet.")
        return pd.DataFrame({
            "Component": [f"PC{i+1}" for i in range(len(self.pca.explained_variance_ratio_))],
            "ExplainedVariance": self.pca.explained_variance_ratio_,
            "CumulativeVariance": self.pca.explained_variance_ratio_.cumsum()
        })

    def plot_variance(self):
        if self.pca is None:
            raise ValueError("PCA not fitted yet.")
        plt.plot(range(1, len(self.pca.explained_variance_ratio_)+1),
                 self.pca.explained_variance_ratio_.cumsum(), marker='o')
        plt.xlabel("Number of Components")
        plt.ylabel("Cumulative Explained Variance")
        plt.title("PCA Explained Variance")
        plt.grid(True)
        plt.show()
