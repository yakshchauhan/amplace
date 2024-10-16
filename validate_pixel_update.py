# import sys

# print(sys.argv)

# with open(sys.argv[0],'r+') as f:
#     print(f.read())
#     f.seek(0)
#     with open("log.txt","w") as lo:
#         for i in f.readlines():
#             lo.write(i)
# exit(-1)
import sys

# Get the paths to the diff file and content file from the arguments
diff_file = sys.argv[1]
content_file = sys.argv[2]

# Open and read the diff file (list of changed files)
with open(diff_file, 'r') as f:
    changes = f.readlines()

# Print or process the list of changed files
print("Changes from the PR:")
for change in changes:
    print(change)

# Open and read the actual content of the modified file (pixel_update.json)
with open(content_file, 'r') as f:
    file_content = f.read()

# Print or process the file content
print("Content of the modified file (pixel_update.json):")
print(file_content)

# Add any additional validation logic based on file content here
# For example, validate the structure of the JSON file
