# Project imports
import twinlab_client as tl

print()  #  Initial white space
dataset = "biscuits.csv"
server = tl.get_command_line_args().server
tl.query_dataset(dataset, server, verbose=True)
