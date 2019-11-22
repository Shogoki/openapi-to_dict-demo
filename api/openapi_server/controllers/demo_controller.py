import connexion
import six

from openapi_server.models.my_model import MyModel  # noqa: E501
from openapi_server import util


def get_demo():  # noqa: E501
    """get_demo

     # noqa: E501


    :rtype: MyModel
    """
    return 'do some magic!'
