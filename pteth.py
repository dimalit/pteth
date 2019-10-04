import web3

globals_to_pass = globals().copy()
locals_to_pass = locals().copy()
del locals_to_pass["globals_to_pass"]

import web3.auto

import sys

import ptpython.repl
import ptpython.layout

provider = None
w3 = None

if len(sys.argv) < 2:

    w3 = web3.auto.w3

    print("Using non-connected local object w3")

else:

    url = sys.argv[1]

    if url.lower().startswith("http"):
        provider = web3.Web3.HTTPProvider(url)
    elif url.lower().startswith("ws"):
        provider = web3.Web3.WebsocketProvider(url)
    else:
        provider = web3.Web3.IPCProvider(url)

    if not provider.isConnected():
        print(f"Cannot connect to {url}")
        exit(1)

    print(f"Connected to {url} via object w3")

    w3 = web3.Web3(provider)

locals_to_pass["w3"] = w3;

def configure(repl):
    repl.show_signature = True
    repl.show_docstring = True
    repl.completion_visualisation = ptpython.layout.CompletionVisualisation.MULTI_COLUMN
    repl.enable_auto_suggest = True
    repl.confirm_exit = False

ptpython.repl.embed(globals_to_pass, locals_to_pass, configure=configure, vi_mode=False, history_filename=None)
