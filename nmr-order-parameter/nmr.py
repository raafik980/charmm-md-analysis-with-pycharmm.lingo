import os
import sys
import pycharmm
import pycharmm.psf as psf
import pycharmm.read as read
import pycharmm.write as write
import pycharmm.settings as settings
import pycharmm.lingo as lingo

from pycharmm.lib import charmm as libcharmm

read.stream('toppar.str')

indcd = 'traj.dcd' 
outdat = 'order.dat'

pycharmm.lingo.charmm_script('open unit 21 write form name ' + outdat ) 
pycharmm.lingo.charmm_script('open unit 62 read unform name ' + indcd )
pycharmm.lingo.charmm_script('TRAJectory QUERy UNIT 62')

nframes = 1125
tmx1 = 3.0

nmr_stream = '''* NMR Order Parameter Calculation
*

NMR
reset
rtimes sele atom * * N end sele atom * * HN end
dyna firstu 62 nunit 1 begin 1 stop 1124 skip 1 tmax 3.0 cut 2.0 ilist 21 dsigma -160.0 C(t)
end
'''
with open('nmr.str', 'w') as f:
    f.write(nmr_stream)


read.stream('nmr.str')


