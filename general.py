import os

# Each website is a separate project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project " + directory)
        os.makedirs(directory)

# Create queue and crawled files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        file_write(queue, base_url)
    if not os.path.exists(crawled):
        file_write(crawled, '')

# Add a new record
def file_write(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# Append to a file
def file_append(path, data):
    file = open(path, 'a')
    file.write(data + '\n')
    file.close()

# Delete file contents
def file_delete(path):
    with open(path, 'w'):
        pass

# Read a file and convert to set
def file_to_set(path):
    links = set()
    with open(path, 'r') as f:
        for line in f:
            links.add(line.replace('\n',''))
    return links

# Convert set to file
def set_to_file(links, file):
    file_delete(file)
    for link in sorted(links):
        file_append(file, link)

        




