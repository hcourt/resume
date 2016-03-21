from __future__ import absolute_import

from resume import freezer
from resume.views import *

if __name__ == '__main__':
    freezer.freeze()
    print "Frozen!"
