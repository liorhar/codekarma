import pysvn
import models

URL = "http://donald/svn/kenshoo2010/trunk/kenshoo/java"


def get_revisions(since_revision):
    client = pysvn.Client()
    end_rev = pysvn.Revision( pysvn.opt_revision_kind.number,
            since_revision+1)
    return client.log(URL, pysvn.Revision( pysvn.opt_revision_kind.head ), end_rev)


