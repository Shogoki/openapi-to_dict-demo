import connexion
import six

from openapi_server.models.my_model import MyModel  # noqa: E501
from openapi_server import util


def get_demo():  # noqa: E501
    """get_demo

     # noqa: E501


    :rtype: MyModel
    """
    # get logger
    app = connexion.FlaskApp("__name__")
    log = app.app.logger

    # create a new instance of MyModel
    model = MyModel(demo_name="name", id=1)
    # Property has snake_case Name: demoName --> demo_name
    log.warn("Model is: {}".format(model))

    # using to_dict method to get a dict from Model
    model_dict = model.to_dict()
    log.warn("Model.to_dict() is: {}".format(model_dict))

    # now we want to convert that dict (probably fetched from DB) back to our Model
    new_model = MyModel.from_dict(model_dict)
    log.warn("New Created Model is: {}".format(new_model))

    return new_model, 200
