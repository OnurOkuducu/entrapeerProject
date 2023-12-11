from celery import Celery
import requests

app = Celery('tasks',broker='amqp://guest:guest@localhost:5672//', 
             backend='rpc://guest:guest@hostname:5672//') 

@app.task
def process_company_data(id):
    url = "https://ranking.glassdollar.com/graphql"
    headers = {
        "Content-Type": "application/json",
    }

    second_query = '''
    query ($id: String!) {
        corporate(id: $id) {
            id
            name
            description
            logo_url
            hq_city
            hq_country
            website_url
            linkedin_url
            twitter_url
            startup_partners_count
            startup_partners {
                master_startup_id
                company_name
                logo_url: logo
                city
                website
                country
                theme_gd
                # Include other fields if needed
            }
            startup_themes
            startup_friendly_badge
        }
    }
    '''

    payload_second_call = {
        "variables": {"id": id},
        "query": second_query,
    }
    try:
        response = requests.post(url, json=payload_second_call, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            # Ignore 500 errors, return None for failed requests
            if response.status_code == 500:
                return None
            else:
                return {"error": f"Failed to fetch data for ID: {id}, Status Code: {response.status_code}"}
    except Exception as e:
        return {"error": f"An error occurred for ID: {id}, Error: {str(e)}"}
