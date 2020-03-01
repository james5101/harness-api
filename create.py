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

def run_query1(query1, variables1):
    request = requests.post(url, json={'query': query1, 'variables':variables1}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

def run_query2(query2):
    request = requests.post(url, json={'query': query2}, headers=headers)
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
    "name": "create_from_api",
    "description": "test create harness application from api"
  }
}

query1 = """
mutation updateGitConfig($gitConfig: UpdateApplicationGitSyncConfigInput!) {
  updateApplicationGitSyncConfig(input: $gitConfig) {
    clientMutationId
    gitSyncConfig {
      branch
      syncEnabled
      gitConnector {
        id
        name
        description
        createdAt
        createdBy {
          id
          name
        }
      }
    }
  }
}

"""
variables1 = {
  "gitConfig": {
    "clientMutationId": "req321",
    "applicationId": "zHvqEutEQ6KcnoG55m8tOg",
    "gitConnectorId": "_pRVp-R_TGqoIC0A60Y7gw",
    "branch": "master",
    "syncEnabled": "true"
  }
}

query2 = """
{
  connectors(
    filters: [
      { connectorType: { operator: EQUALS, values: GIT } }
    ]
    limit: 10
  ) {
    pageInfo {
      total
    }
    nodes {
      id
      name
    }
  }
}
"""
# result = run_query(query, variables) 
# result1 = run_query(query1,variables1)
result2 = run_query2(query2)
print(result2)
