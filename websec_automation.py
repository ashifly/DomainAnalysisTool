import subprocess
import re

input_file = "input_file.txt"
httpx_output = "httpx_results.txt"
filtered_subdomains = "filtered_subdomains.txt"
modified_urls = "modified_urls.txt"
cdncheck_output = "cdncheck_results.txt"
merged_subdomains = "output.txt"
inactive_subdomains_file = "inactive_subdomains.txt"

# Step 1: Use httpx to check status codes and save results
subprocess.run(["httpx", "-l", input_file, "-silent", "-status-code", "-o", httpx_output])

# Step 1.5: Remove dot from the end of each line
with open(httpx_output, "r") as file:
    lines = file.readlines()
    lines = [line.rstrip('.') for line in lines]

with open(httpx_output, "w") as file:
    file.writelines(lines)

# Step 2: Filter subdomains
with open(httpx_output, "r") as file:
    lines = file.readlines()
    subdomains = [line.split()[0] for line in lines]

with open(filtered_subdomains, "w") as file:
    file.writelines("\n".join(subdomains))

# Step 3: Remove "https://" and "http://"
with open(filtered_subdomains, "r") as file:
    lines = file.readlines()
    lines = [line.replace("https://", "").replace("http://", "") for line in lines]

with open(filtered_subdomains, "w") as file:
    file.writelines(lines)

# Step 4: Use cdncheck to check for CDNs
subprocess.run(["cdncheck", "-i", filtered_subdomains, "-resp", "-o", cdncheck_output])

# Step 5: Merge all the subdomains with status code and cdn
with open(filtered_subdomains, "r") as file1, open(httpx_output, "r") as file2, open(cdncheck_output, "r") as file3, open(merged_subdomains, "w") as output_file:
    for line1 in file1:
        subdomain1 = line1.strip()

        # Find matching lines in file2 (httpx results)
        file2.seek(0)  # Move the cursor to the beginning of file2
        matching_line2 = next((line2.strip() for line2 in file2 if subdomain1 in line2), None)

        # Find matching lines in file3 (cdncheck results)
        file3.seek(0)  # Move the cursor to the beginning of file3
        matching_line3 = next((line3.strip() for line3 in file3 if subdomain1 in line3), None)

        # If both matches are found, merge and write to the output file
        if matching_line2 and matching_line3:
            cdn_info = ' '.join(re.findall(r'\[.*?\]', matching_line3))
            merged_line = f"{matching_line2} {cdn_info}\n"
            output_file.write(merged_line)
        elif matching_line2:
            output_file.write(f"{matching_line2} \n")

#Finding Inactive Domains
# Step 6: Read subdomains from input_file
with open(input_file, "r") as file:
    all_subdomains = {line.strip() for line in file}

# Step 7: Read subdomains from httpx_output
with open(httpx_output, "r") as file:
    httpx_subdomains = {line.split()[0].strip().replace("https://", "").replace("http://", "") for line in file}
# Step 8: Find subdomains not present in httpx_output
inactive_subdomains = all_subdomains - httpx_subdomains

# Step 9: Write inactive subdomains to a file
with open(inactive_subdomains_file, "w") as file:
    file.write("\n".join(inactive_subdomains))


print("Script completed successfully.")
