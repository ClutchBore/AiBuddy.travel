import logging
import openai
import azure.functions as func

#sample request
# {"model":"text-davinci-003", "prompt":"give me a slogan for rouse high school at leander isd in leander, tx", "max_tokens":200, "temperature":0}
secret_key='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'
def main(req: func.HttpRequest) -> func.HttpResponse:
   
    logging.info('Python HTTP trigger function processed a request.')
    openai.api_key=secret_key
   
    req_body=req.get_json()
    logging.info(type(req_body))   
    localprompt=req_body['prompt']
    localprompt=localprompt+'at Rouse highschool under Leander ISD '
    output=openai.Completion.create(
        model=req_body['model'],
        prompt=localprompt,
        max_tokens=req_body['max_tokens'],
        temperature=req_body['temperature']
    )
    output_text=output['choices'][0]['text']
    return func.HttpResponse(output_text, status_code=200)
     