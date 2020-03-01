import requests
import os

url = "https://app.harness.io/gateway/api/graphql?accountId=R3L-GcfkSqqZTG7_CWR4-w"

headers = {
  'Content-Type': 'application/json',
  'X-Api-Key': (os.environ.get('HARNESS_API_KEY'))
}

def run_query(query, variables):
    request = requests.post(url, json={'query': query, 'variables':variables}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

             
query = """
mutation createapp($app: CreateApplicationInput!) {
  createApplication(input: $app) {
    clientMutationId
    application {
      name
      id
    }
  }
}

"""
variables = {
  "app": {
    "clientMutationId": "req9",
    "name": "create_from_api_3",
    "description": "test create harness application from api"
  }
}

result = run_query(query, variables) 
print(result)
