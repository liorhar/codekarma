import models
from codekarma import app
try:
    from pysvn import Client, opt_revision_kind, Revision
except:
    from codekarma.dummysvn import Client


def get_revisions(since_revision):
    client = Client()
    end_rev = Revision(opt_revision_kind.number,
            since_revision + 1)
    return client.log(app.config["SVN_URL"], Revision(opt_revision_kind.head),
        end_rev)
