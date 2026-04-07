🛡️ Sentinel-AI
Sentinel-AI is a machine learning-driven security analysis tool designed to identify malicious web traffic within standard HTTP server logs. It moves beyond traditional static rules by using statistical isolation to find "hidden" threats.

⚙️ How It Works
The system follows a 4-step pipeline to transform raw text into security insights:

Log Parsing (Regex): The script uses optimized Regular Expressions to scan access.log files. It instantly converts unstructured strings into a structured Pandas DataFrame.

Feature Engineering: To help the AI "understand" the traffic, we extract numerical features:

URL Length: Long, complex strings often indicate buffer overflow or injection attempts.

SQL Signatures: A boolean flag (Is Sql) that triggers when keywords like UNION or SELECT are detected.

Status Codes: High frequencies of 403 (Forbidden) or 404 (Not Found) usually signal directory brute-forcing.

The Brain (Isolation Forest): Instead of teaching the AI what a "bad" request looks like, we use an unsupervised model. It assumes that normal traffic is frequent and similar. Anything that is "different" (an outlier) is isolated and labeled as an anomaly (-1).

Visualization: Using Seaborn, the tool maps every request on a 2D plane. This allows humans to visually confirm attack clusters at a glance.

🛠️ Installation & Setup
Follow these steps to deploy Sentinel-AI on your local environment:

1. Clone & Navigate
Bash
git clone https://github.com/Harutt0/Sentinel-AI
cd Sentinel-AI

3. Environment Setup
Install the required data science and machine learning libraries:

Bash
pip install pandas seaborn scikit-learn matplotlib

3. Data Preparation
Place your target log file (e.g., access.log) into the project root directory. Ensure the file follows the standard Nginx/Apache combined log format.

4. Execution
Run the analysis engine:

Bash
python main.py
📊 Understanding the Output
Once executed, Sentinel-AI provides two types of feedback:

Console Report: A filtered table showing the Top 10 most suspicious IP addresses and their activities.

Anomaly Map: An interactive plot where Red dots represent identified threats and Green dots represent legitimate traffic.

🎯 Use Cases
Incident Response: Quickly identify the source of a DDoS or SQLi attack.

Security Auditing: Scan historical logs to find missed breaches.

Zero-Day Detection: Find unusual patterns that signature-based Firewalls might miss.
