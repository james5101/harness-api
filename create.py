import requests
import os
account_key = (os.environ.get('HARNESS_ACCOUNT_KEY'))

url = f"https://app.harness.io/gateway/api/graphql?accountId={account_key}"

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
    "name": "create_from_api_4",
    "description": "test create harness application from api"
  }
}

result = run_query(query, variables) 
print(result)
