from subprocess import call
from string import Template
import os

testDir = os.path.dirname(os.path.realpath(__file__))
pythonPath = Template('--pythonpath ${entry}')

rfexec  = "pybot"
params  = ' '.join([
	pythonPath.substitute(entry="%s/../src" % testDir),
	'--outputdir ' + testDir + '/results'
])
tests   = testDir + '/integration'

if os.name == 'nt':
	rfexec += '.bat'

command = "{0} {1} {2}".format(rfexec, params, tests)

call(command, env=os.environ)
