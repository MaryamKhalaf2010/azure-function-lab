import logging
import azure.functions as func

app = func.FunctionApp()

# --- Function 1: HTTP to Queue ---
@app.function_name(name="HttpToQueue")
@app.route(route="HttpToQueue", auth_level=func.AuthLevel.ANONYMOUS)
@app.queue_output(arg_name="msg", queue_name="myqueue-items", connection="AzureWebJobsStorage")
def HttpToQueue(req: func.HttpRequest, msg: func.Out[str]) -> func.HttpResponse:
    logging.info("Processing HttpToQueue request.")
    
    try:
        req_body = req.get_json()
        name = req_body.get("name")
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    if name:
        msg.set(f'{{"name": "{name}"}}')
        return func.HttpResponse(f"Sent '{name}' to Azure Queue.")
    else:
        return func.HttpResponse("Missing 'name' in request", status_code=400)


# --- Function 2: HTTP to SQL ---
@app.function_name(name="HttpToSql")
@app.route(route="HttpToSql", auth_level=func.AuthLevel.ANONYMOUS)
@app.sql_output(
    arg_name="outputSql",
    command_text="dbo.Person",  # <- Important: just table name here
    connection_string_setting="SqlConnectionString")
def HttpToSql(req: func.HttpRequest, outputSql: func.Out[func.SqlRow]) -> func.HttpResponse:
    logging.info("Processing HttpToSql request.")

    try:
        req_body = req.get_json()
        name = req_body.get("name")
        city = req_body.get("city")
    except ValueError:
        return func.HttpResponse("Invalid JSON input", status_code=400)

    if not name or not city:
        return func.HttpResponse("Missing 'name' or 'city'", status_code=400)

    outputSql.set(func.SqlRow({"Name": name, "City": city}))
    return func.HttpResponse(f"Inserted: {name} from {city}", status_code=200)
