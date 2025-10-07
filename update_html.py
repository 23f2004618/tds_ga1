import json

# Read the email from email.json
with open('email.json', 'r') as f:
    data = json.load(f)
    email = data['email']

# Read the content of index.html
with open('index.html', 'r') as f:
    html_content = f.read()

# Replace the placeholder with the email
# The placeholder is <!--email_off-->...<!--/email_off-->
start_tag = '<!--email_off-->'
end_tag = '<!--/email_off-->'
start_index = html_content.find(start_tag)
end_index = html_content.find(end_tag)

if start_index != -1 and end_index != -1:
    placeholder = html_content[start_index + len(start_tag):end_index]
    html_content = html_content.replace(start_tag + placeholder + end_tag, email)

# Correct the <hq> tag to <h1>
html_content = html_content.replace('<hq>', '<h1>')
html_content = html_content.replace('</hq>', '</h1>')

# Write the updated content back to index.html
with open('index.html', 'w') as f:
    f.write(html_content)

print("index.html has been updated successfully.")