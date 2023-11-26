🚀 **Domain Analysis Toolkit**

### Overview
This powerful Python script empowers you to comprehensively analyze a list of subdomains, providing invaluable insights into their HTTP status codes, CDN presence, and inactive status. Leveraging renowned tools like httpx and cdncheck, this script ensures a thorough examination of your subdomain ecosystem.

### Features
1. **HTTP Status Code Check 🌐**
   - Utilizes httpx to swiftly check the HTTP status codes for each subdomain.
   - Saves the detailed results to a file for reference (httpx_results.txt).

2. **Subdomain Filtering 🧹**
   - Cleanses subdomains by removing trailing dots.
   - Filters out unnecessary prefixes like "https://" and "http."
   - Outputs a pristine list of subdomains to a dedicated file (filtered_subdomains.txt).

3. **CDN Check 🚀**
   - Harnesses the power of cdncheck to identify Content Delivery Networks associated with each subdomain.
   - Archives CDN check results for further analysis (cdncheck_results.txt).

4. **Merging Subdomains 🤝**
   - Seamlessly combines subdomains with their corresponding HTTP status codes and CDN information.
   - Creates a consolidated report, saving it to a user-friendly file (output.txt).

5. **Finding Inactive Subdomains 🕵️‍♂️**
   - Compares the original subdomain list with httpx results to pinpoint inactive subdomains.
   - Outputs a dedicated file highlighting inactive subdomains (inactive_subdomains.txt).

### Usage
1. **Prepare Your List**
   - Place your list of subdomains in a file named `input_file.txt`.

2. **Execute the Script**
   - Run the `domain_analysis.py` script.

### Requirements
- Python 3.x
- Dependencies: httpx (Install using: `pip install httpx`), cdncheck (Install using: `pip install cdncheck`)

### File Descriptions
- **input_file.txt:** Your source file containing the list of subdomains.
- **httpx_results.txt:** Archive of HTTP status code results.
- **filtered_subdomains.txt:** Refined list of subdomains after filtering.
- **cdncheck_results.txt:** Compilation of CDN check results.
- **output.txt:** Merged report with subdomains, status codes, and CDN information.
- **inactive_subdomains.txt:** List of identified inactive subdomains.

Experience a seamless and insightful subdomain analysis with this toolkit. Happy exploring! 🚀🔍
