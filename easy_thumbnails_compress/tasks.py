from celery.task import  Task
from django.conf import settings
import os
import subprocess
import logging
logger = logging.getLogger(__name__)

class CompressImage(Task):
    """
    compresses an image with trimage
    """
    def run(self, sender, **kwargs):
        """
        Run the task
        """
        path = os.path.join(settings.MEDIA_ROOT, str(sender))
        callcmd = []
        callcmd.append('trimage')
        callcmd.append('-q')
        callcmd.append('--file={0}'.format(path))
        p = subprocess.call(callcmd, close_fds=True, env=os.environ )

        logger.debug("compressing: {0}".format(path))
        logger.debug(p)