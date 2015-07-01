from subprocess import call
from string import Template
import os

pythonPath = Template('--pythonpath ${entry}')

rfexec  = "pybot"
params  = [
	pythonPath.substitute(entry="{file}/../src".format(__file__))
].join(' ')
tests   = "./test/integration"

if os.name == 'nt':
	rfexec += '.bat'

command = "{0} {1} {2}".format(rfexec, params, tests)

call(command, env=os.environ)
