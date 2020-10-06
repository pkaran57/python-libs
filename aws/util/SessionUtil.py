import boto3

from definitions import *


def get_session():
    """
    Session objects are not thread safe and should not be shared across threads and processes.
    You should create a new Session object for each thread or process.
    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/session.html#multithreading-or-multiprocessing-with-sessions
    :return: new instance of a session
    """
    return boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                 aws_session_token=AWS_SESSION_TOKEN,
                                 region_name=AWS_REGION)
