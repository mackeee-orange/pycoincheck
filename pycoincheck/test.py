import pycoincheck

api = pycoincheck.API(api_key="68cMRWmHY6eM5h8k", api_secret="lPLxyJCLoBPl_LeapTHF9ptjFKpysvzJ")

board = api.board()
print(board)