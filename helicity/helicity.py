# Importing pcharmm libraries

import pycharmm
import pycharmm.psf as psf
import pycharmm.read as read
import pycharmm.write as write
import pycharmm.settings as settings
import pycharmm.lingo as lingo

from pycharmm.lib import charmm as libcharmm


# Load the topology files using pyCHARMM  
read.stream('toppar.str')

# Load the psf file using psf_card in pyCHARMM
read.psf_card('traj.psf')
psf.get_nres()


#Define the input and output files
#Input: trajectory file
#Output: order parameter file

#remove the old order.dat file
import os
if os.path.exists('helicity.dat'):
    os.remove('helicity.dat')

indcd = 'traj.dcd' 
outdat = 'helicity.dat'


#CHARMM units are used to read and write files
pycharmm.lingo.charmm_script('open unit 21 write form name ' + outdat ) 
pycharmm.lingo.charmm_script('open unit 62 read unform name ' + indcd )

#Print Trajectory Information
pycharmm.lingo.charmm_script('TRAJectory QUERy UNIT 62') 


#CHARMM STtream File Generation for NMR Module, Set options for NMR module
helicity_stream = '''* Helicity Calculation             !! * TITLE      : SYNTAX REQUIRED FOR STREAM
*                                                       !! *            :SYNTAX REQUIRED FOR STREAM
                                                        !! <EMPTY_LINE> : SYNTAX REQUIRED FOR STREAM  
CORREL MAXTIME 300000 MAXSERIES 10                                !! CORREL START: MAXTIME SHOULD BE MORE THAN THE ACTUAL NUMBER OF SNAPSHOTS IN DCD 
    ENTER V1 HELIX SELECT SEGID PROA -
    .AND. ( RESID 161:173 ) - 
    .AND. ( atom * * O .or. atom * * C .or. atom * * CA .or. atom * * N ) END                       !!
    TRAJ FIRSTU 62 NUNIT 1 BEGIN 1 ! STOP 1124 SKIP 1       !!
    WRITE V1 DUMB TIME UNIT 21                          !!
END                                                     !! CORREL END  

return
'''
with open('helicity.str', 'w') as f:
    f.write(helicity_stream)

# Running NMR Module via read option in pyCHARMM
read.stream('helicity.str')
#pycharmm.lingo.charmm_script('stream helcity.str')



