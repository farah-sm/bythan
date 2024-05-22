import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get GitHub PAT from environment variables
access_token = os.getenv('GITHUB_PAT')
org_name=os.getenv('GITHUB_ORG')

if not access_token:
    print('GitHub Personal Access Token not found in .env file')
    exit(1)

# GitHub API base URL
param = { 'type' : 'private'}
header = {'Authorization' : f'Bearer {access_token}'}

api_url = f'https://api.github.com/orgs/{org_name}/repos'

# Write your script here and output the results to the console.
response = requests.get(api_url, params = param, headers = header)


for i in response.json():
    print(i["name"])
