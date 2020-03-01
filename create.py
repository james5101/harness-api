import requests
import os
account_key = (os.environ.get('HARNESS_ACCOUNT_KEY'))

url = f"https://app.harness.io/gateway/api/graphql?accountId={account_key}"

headers = {
  'Content-Type': 'application/json',
  'X-Api-Key': (os.environ.get('HARNESS_API_KEY'))
}

def run_query_with_vars(query, variables):
  request = requests.post(url, json={'query': query, 'variables':variables}, headers=headers)
  if request.status_code == 200:
    return request.json()
  else:
    raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

def run_query_without_vars(query):
  request = requests.post(url, json={'query': query}, headers=headers)
  if request.status_code == 200:
    return request.json()
  else:
    raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

def get_git_connector_by_id(name):
  query = """
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
  result = run_query_without_vars(query)
  print(result)

def create_new_application(name, description):
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
        "name": name,
        "description": description
    }
  }
  result = run_query_with_vars(query, variables)
  print(result)

def create_git_sync_with_app(name):
  query = """
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
  variables = {
    "gitConfig": {
      "clientMutationId": "req321",
      "applicationId": "zHvqEutEQ6KcnoG55m8tOg",
      "gitConnectorId": "_pRVp-R_TGqoIC0A60Y7gw",
      "branch": "master",
      "syncEnabled": "true"
    }
  }
  result = run_query_with_vars(query, variables)
  print(result)
# get_git_connector_by_id("test")
# create_new_application("name")
# create_git_sync_with_app("name")
create_new_application("test_create", "description")
