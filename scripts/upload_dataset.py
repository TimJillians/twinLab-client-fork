# Standard imports
import os

# Project imports
import twinlab as tl

print()  #  Initial white space
file = os.path.join("datasets", "biscuits.csv")
server = tl.get_command_line_args().server
tl.upload_dataset(file, server=server, verbose=True, debug=True)
