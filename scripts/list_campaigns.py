# Project imports
import twinlab_client as tl

print()  #  Initial white space
server = tl.get_command_line_args().server
tl.list_campaigns(server, verbose=True)
