# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import os
import argparse
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand
from boto3.session import Session


def valid_date(s):
    """
    from http://stackoverflow.com/questions/25470844/specify-format-for-input-arguments-argparse-python
    """
    try:
        return datetime.strptime(s, "%Y_%m_%d_%H%M_UTC")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


class Command(BaseCommand):
    help = 'Restores PostgreSQL database from AWS S3'

    def add_arguments(self, parser):
        parser.add_argument('datetime',
            action='store',
            nargs='?',
            default=datetime.utcnow().strftime('%Y_%m_%d_%H%M_UTC'),
            help='Target UTC Datetime for restore from first earlier backup. Format: %Y_%m_%d_%H%M_UTC'
        )

    def handle(self, *args, **options):

        # AWS_ACCESS_KEY_ID = os.environ.get('AWS_S3_ACCESS_KEY_ID')
        # AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_S3_SECRET_ACCESS_KEY')
        # AWS_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
        # AWS_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')
        #
        # session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
        #                   aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        #                   region_name=AWS_REGION_NAME)
        #
        # s3 = session.resource('s3')
        db_datetime = valid_date(options.get('datetime'))
        db_filename = "pgbackup_{}.dump".format(db_datetime)
        import ipdb; ipdb.set_trace()
        #
        # bucket = s3.Bucket(AWS_BUCKET_NAME)
        # bucket.download_file(db_filename, db_filename)