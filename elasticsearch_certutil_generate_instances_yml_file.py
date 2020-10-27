
# This will create an output file of instances.yml.

input_file = open("elk-servers.txt", "r")
servers = input_file.readlines()

output_file = open("instances.yml", "w")
output_file.write("instances:\n")

for server in servers:
    output_file.write("  - name: \"" + server.split()[0] + "\"\n\
    ip:\n\
      - \"" + server.split()[1] + "\"\n\
      - \"" + server.split()[2] + "\"\n\
    dns:\n\
      - \"elasticsearch\"\n\
      - \"localhost\"\n\
      - \"" + server.split()[0] + ".company.com\"\n\
      - \"" + server.split()[0] + "\"\n")
    output_file.write("\n")

output_file.close()
