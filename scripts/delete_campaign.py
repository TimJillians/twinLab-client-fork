# Project imports
import twinlab_client as tl

print()  #  Initial white space
campaign = "biscuits-python"
server = tl.get_command_line_args().server
tl.delete_campaign(campaign, server, verbose=True)
