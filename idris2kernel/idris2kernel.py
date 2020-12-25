from ipykernel.kernelbase import Kernel
from pexpect import replwrap

class Idris2Kernel(Kernel):
    implementation = 'Idris2 REPL'
    implementation_version = '0.1'
    language = 'idris2'
    language_version = '0.2.1'
    language_info = {
        'name': 'Idris2',
        'mimetype': 'text/x-idr',
        'file_extension': '.idr'
    }
    banner = "Idris2 REPL IPython Kernel"

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.idris2repl = replwrap.REPLWrapper("idris2", "Main> ", None)

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        if not silent:
            stream_content = {'name': 'stdout', 'text': self.idris2repl.run_command(code)}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
        }
