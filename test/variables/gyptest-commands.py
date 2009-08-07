#!/usr/bin/env python

"""
Test variable expansion of '<!()' syntax commands.
"""

import TestGyp

test = TestGyp.TestGyp(format='gypd')

expect = """\
GENERAL: running with these options:
GENERAL:   msvs_version: None
GENERAL:   suffix: ''
GENERAL:   includes: None
GENERAL:   depth: '.'
GENERAL:   generator_flags: []
GENERAL:   formats: ['gypd']
GENERAL:   debug: ['variables', 'general']
GENERAL:   defines: None
VARIABLES: Expanding 'import math; print math.pi' to 'import math; print math.pi'
VARIABLES: Expanding 'ABCD' to 'ABCD'
VARIABLES: Expanding 'python -c "print 'letters'"' to 'python -c "print 'letters'"'
VARIABLES: Executing command 'python -c "print 'letters'"'
VARIABLES: Expanding '<!(python -c "print 'letters'")' to 'letters'
VARIABLES: Expanding '<(<!(python -c "print 'letters'"))' to 'ABCD'
VARIABLES: Expanding 'pi' to 'pi'
VARIABLES: Expanding '["python", "-c", "<(pi)"]' to '["python", "-c", "import math; print math.pi"]'
VARIABLES: Executing command '['python', '-c', 'import math; print math.pi']'
VARIABLES: Expanding '<!(["python", "-c", "<(pi)"])' to '3.14159265359'
VARIABLES: Expanding 'letters' to 'letters'
VARIABLES: Expanding 'python -c "print '<(letters)'"' to 'python -c "print 'ABCD'"'
VARIABLES: Executing command 'python -c "print 'ABCD'"'
VARIABLES: Expanding '<!(python -c "print '<(letters)'")' to 'ABCD'
VARIABLES: Expanding 'letters' to 'letters'
VARIABLES: Expanding 'letters' to 'letters'
VARIABLES: Expanding 'pi' to 'pi'
VARIABLES: Expanding 'python -c "<(pi)"' to 'python -c "import math; print math.pi"'
VARIABLES: Executing command 'python -c "import math; print math.pi"'
VARIABLES: Expanding 'python -c "print '<!(python -c "<(pi)") <(letters)'"' to 'python -c "print '3.14159265359 ABCD'"'
VARIABLES: Executing command 'python -c "print '3.14159265359 ABCD'"'
VARIABLES: Expanding '<!(python -c "print '<!(python -c "<(pi)") <(letters)'")' to '3.14159265359 ABCD'
VARIABLES: Expanding 'foo' to 'foo'
VARIABLES: Expanding 'none' to 'none'
VARIABLES: Expanding 'test_action' to 'test_action'
VARIABLES: Expanding 'echo' to 'echo'
VARIABLES: Expanding '_inputs' to '_inputs'
VARIABLES: Expanding 'var2' to 'var2'
VARIABLES: Expanding '<(var2)' to '3.14159265359 ABCD'
VARIABLES: Expanding '<(_inputs)' to '"3.14159265359 ABCD"'
VARIABLES: Expanding '_outputs' to '_outputs'
VARIABLES: Expanding 'var4' to 'var4'
VARIABLES: Expanding '<(var4)' to 'ABCD'
VARIABLES: Expanding '<(_outputs)' to 'ABCD'
VARIABLES: Expanding '3.14159265359 ABCD' to '3.14159265359 ABCD'
VARIABLES: Expanding 'ABCD' to 'ABCD'
VARIABLES: Expanding 'commands.gyp' to 'commands.gyp'
VARIABLES: Expanding 'ABCD' to 'ABCD'
VARIABLES: Expanding '3.14159265359' to '3.14159265359'
VARIABLES: Expanding 'ABCD' to 'ABCD'
VARIABLES: Expanding '3.14159265359 ABCD' to '3.14159265359 ABCD'
VARIABLES: Expanding 'foo' to 'foo'
VARIABLES: Expanding 'none' to 'none'
VARIABLES: Expanding 'test_action' to 'test_action'
VARIABLES: Expanding 'echo' to 'echo'
VARIABLES: Expanding '"3.14159265359 ABCD"' to '"3.14159265359 ABCD"'
VARIABLES: Expanding 'ABCD' to 'ABCD'
VARIABLES: Expanding '3.14159265359 ABCD' to '3.14159265359 ABCD'
VARIABLES: Expanding 'ABCD' to 'ABCD'
"""

test.run_gyp('commands.gyp',
             '--debug', 'variables', '--debug', 'general',
             stdout=expect)

test.must_match('commands.gypd', test.read('commands.gypd.golden'))

test.pass_test()