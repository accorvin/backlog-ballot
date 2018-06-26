#! /usr/bin/env python

import jira
import os
import requests


JIRA_QUERY = os.environ['BACKLOG_BALLOT_QUERY']
JIRA_SERVER = os.environ['BACKLOG_BALLOT_JIRA_SERVER']
BACKLOG_BALLOT_BACKEND = os.environ['BACKLOG_BALLOT_BACKEND']

client_args = {
    'server': JIRA_SERVER,
    'options': dict(verify=False),
}
client = jira.client.JIRA(**client_args)
issues = client.search_issues(JIRA_QUERY, maxResults=False)

for issue in issues:
    title = issue.fields.summary
    description = issue.fields.description
    created = issue.fields.created
    jira_issue_url = issue.permalink()
    jira_key = issue.key

    exists_data = {'jiraKey': jira_key}
    r = requests.post(BACKLOG_BALLOT_BACKEND + '/api/issues/exists',
                      json=exists_data)
    exists = r.json()['exists']
    if exists:
        msg = 'Issue {key} already exists, skipping'
        print(msg.format(key=jira_key))
        continue
    else:
        msg = 'Issue {key} does not exist, attempting to create'
        print(msg.format(key=jira_key))
        create_data = {
            'title': title,
            'description': description,
            'created': created,
            'jira_issue_url': jira_issue_url,
            'jira_key': jira_key
        }
        r = requests.post(BACKLOG_BALLOT_BACKEND + '/api/issues/new',
                          json=create_data)
        if r.status_code == 201 and \
           r.json()['code'] == 'success':
            print('Issue was successfully created')
        else:
            print('Issue could not be created')
