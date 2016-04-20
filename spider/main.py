"""The web spider that aggregates data."""

import requests
import zlib

from threading import Thread
from queue import Queue

import boto3


class Work:
    """Caches queued web-urls."""

    def __init__(self):
        """Poll SQS, and thread messages."""

        # AWS-Clients
        self.sqs = boto3.resource('sqs')
        self.s3 = boto3.resource('s3')

        # SQS queue.
        self.queue = self.sqs.get_queue_by_name(QueueName='spider_domains')

        # Populate some data for testing.
        entries = [{'Id': str(n), 'MessageBody': 'string'} for n in range(10)]
        self.queue.send_messages(Entries=entries)

        # Worker loop.
        self.do_work = True
        self. i = 1
        while self.do_work:
            self.work()

    def work(self):
        """Do nothing."""
        print(self.i)
        self.i += 1

        messages = self.queue.receive_messages(MaxNumberOfMessages=1)
        if messages.__len__() > 0:
            message = messages[0]
            message.delete()
        else:
            self.do_work = False

    def download(self, url):
        """Get the HTML of a URL and put it in S3."""

        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible)',
            'From': ''
        }

        response = requests.get(url, headers=headers)
        html = response.content

        args = {
            'key': None,  # TODO
            'body': bytes(html),
            'bucket': 'anavahspider',
            'ContentLength': html.__len__()
        }
        self.s3.put_object(**args)


def main():
    """I bet this'll be depreceated by publishing."""

    w = Work()


if __name__ == '__main__':
    main()
