# Project imports
import twinlab as tl

print()  #  Initial white space
dataset = "biscuits.csv"
server = tl.get_command_line_args().server
tl.delete_dataset(dataset, server, verbose=True)
