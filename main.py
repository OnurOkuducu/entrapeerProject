from celery.result import GroupResult
from fastapi import FastAPI
from celery import group
from tasks import process_company_data
import json

app = FastAPI()

@app.get("/execute_tasks")
def execute_tasks():
    file_path = './output.json'

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    id_arr = data.keys()

    results_dict = {} 

    for company_id in id_arr:
        result = process_company_data.delay(data[company_id])
        task_result = result.get(propagate=False) 

        results_dict[company_id] = task_result


    return results_dict


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
