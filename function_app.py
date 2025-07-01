import azure.functions as func
import logging
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        # If a name is provided, queue a message to the queue
        queue_message = {
            'name': name,
            'source': 'http_trigger'
        }

        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )


@app.route(route="custom_trigger")
def custom_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python custom trigger function processed a request.')
    # Let's read an environment variable for demonstration
    custom_value = os.getenv('CUSTOM_KEY', 'default_value')
    return func.HttpResponse(
        f"CUSTOM_KEY value is: {custom_value}",
        status_code=200
    )


@app.function_name(name="queue_trigger")
@app.queue_trigger(arg_name="msg", queue_name="my-queue", connection="AzureWebJobsStorage")
def queue_trigger(msg: func.QueueMessage) -> None:
    logging.info(
        f'Queue trigger function processed a message: {msg.get_body().decode()}')
