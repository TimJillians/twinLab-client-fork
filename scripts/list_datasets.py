# Project imports
import twinlab as tl

print()  #  Initial white space
server = tl.get_command_line_args().server
_ = tl.list_datasets(server=server, verbose=True, debug=True)
