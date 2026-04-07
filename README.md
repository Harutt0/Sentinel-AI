# 🛡️ Sentinel-AI
**Sentinel-AI** is a high-performance, Machine Learning-driven log analysis tool developed in Python. It proactively identifies malicious web traffic by isolating anomalies in HTTP logs using the **Isolation Forest** algorithm.
-----

### 🎯 Project Overview
The objective of this project is to provide an intelligent security layer that moves beyond static rules. **Sentinel-AI** demonstrates how **Unsupervised Machine Learning** can be applied to cybersecurity to detect zero-day exploits, SQL injections, and unusual scanning patterns by analyzing behavioral deviations in web traffic.

### ✨ Key Features
  * **ML-Driven Detection:** Uses the `Isolation Forest` algorithm to identify threats without needing predefined attack signatures.
  * **Feature Engineering:** Automatically extracts critical metrics like URL length, HTTP status codes, and SQLi patterns.
  * **High-Speed Parsing:** Optimized `Regex` engine to process large `access.log` files efficiently.
  * **Interactive Visualization:** Generates statistical scatter plots to visually separate attackers (anomalies) from legitimate users.
  * **Error Resilient:** Advanced data validation to handle malformed log entries and corrupted data.

-----
### 🛠️ Technical Stack
| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.11+ |
| **ML Engine** | `scikit-learn` (Isolation Forest) |
| **Data Science** | `pandas`, `numpy` |
| **Visualization** | `seaborn`, `matplotlib` |
| **Parsing** | `re` (Regular Expressions) |

-----
### 🚀 Getting Started

#### 1\. Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/CryzZ1/Sentinel-AI.git
cd Sentinel-AI
```

#### 2\. Install Dependencies
Install the required machine learning and data processing libraries:

```bash
pip install -r requirements.txt
```

#### 3\. Run Analysis
Place your `access.log` file in the root directory and execute:

```bash
python main.py
```

-----

### 🛠️ Technical Specifications
> **Note:** This project prioritizes analytical depth. It transforms unstructured raw logs into a 4-dimensional feature matrix for precise anomaly scoring.

  * **Isolation Forest:** Builds an ensemble of isolation trees to identify outliers with fewer splits.
  * **Signature Analysis:** Integrated detection for `UNION`, `SELECT`, and `OR 1=1` patterns.
  * **Performance:** Leverages `pandas` vectorized operations for near-instant analysis of thousands of rows.

-----
### 🙏 Acknowledgements

  * Inspired by professional SIEM and IDS logic used in modern SOC environments.
  * Thanks to the Scikit-Learn community for providing robust anomaly detection frameworks.

**Thank you for checking out this project\! If you like it, feel free to leave a ⭐.**

**Developed with passion for a safer web by Harutt0** 🚀
