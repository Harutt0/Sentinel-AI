import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

def parseLogsFast(filePath):
    # Regex pattern to extract: IP, Date, Method, URL, and Status Code
    logPattern = r'(\S+) \S+ \S+ \[(.*?)\] "(\S+) (\S+) \S+" (\d+) \d+'
    try:
        # Loading logs into a DataFrame using the regex separator
        df = pd.read_csv(
            filePath, 
            sep=logPattern, 
            engine='python', 
            usecols=[1, 3, 4, 5], 
            names=['Ip', 'method', 'url', 'status'],
            header=None
        )

        # Calculate the length of the requested URL (Long URLs are often suspicious)
        df['Url Len'] = df['url'].str.len()

        # Convert HTTP method to binary (POST=1, others=0)
        df['Is Post'] = (df['method'] == 'POST').astype(int)

        # Ensure HTTP Status codes are treated as numbers
        df['Status'] = pd.to_numeric(df['status'], errors='coerce')

        # Signature-based detection: Check for common SQL Injection keywords
        sqlKeywords = "'|--|select|union"
        df['Is Sql'] = df['url'].str.lower().str.contains(sqlKeywords, regex=True).astype(int)

        return df.dropna()
    
    except FileNotFoundError:
        print(f"Error: {filePath} Not found!")
        return None
    
def visualizeAnomalies(df):
    """
    Generates a 2D scatter plot to visualize how the model separated 
    anomalous traffic from normal traffic.
    """
    plt.figure(figsize=(12, 6))
    sns.set_theme(style="darkgrid")
    
    # Plotting: URL Length vs Status Code, colored by the Anomaly Score
    scatter = sns.scatterplot(
        data=df, 
        x='Url Len', 
        y='Status', 
        hue='Anomaly Score', 
        palette={1: '#2ecc71', -1: '#e74c3c'}, # Green for Normal, Red for Anomaly
        s=100,
        alpha=0.7
    )
    
    plt.title('Sentinel-AI', fontsize=15)
    plt.xlabel('URL Length', fontsize=12)
    plt.ylabel('Http Status Code', fontsize=12)
    plt.legend(title='Status', labels=['Normal (1)', 'Anomaly (-1)'])
    plt.show()

if __name__ == "__main__":
    logFile = 'access.log'
    df = parseLogsFast(logFile)
    if df is not None:
        print(f"--- {len(df)} Line Log Loaded ---")

        # Selecting the numerical columns for the ML model
        features = ['Url Len', 'Is Post', 'Status', 'Is Sql']

        # contamination=0.03 assumes 3% of the data is expected to be anomalous
        model = IsolationForest(contamination=0.03, random_state=42)

        # Fit the model and predict (-1 for anomalies, 1 for normal)
        df['Anomaly Score'] = model.fit_predict(df[features])

        # Filter and display the identified security threats
        anomalies = df[df['Anomaly Score'] == -1]
        print(f"\n[!] Number of Suspects Identified: {len(anomalies)}")
        print(anomalies[['Ip', 'Url Len', 'Status', 'Is Sql']].head(10))

        # Launch visualization
        visualizeAnomalies(df)
