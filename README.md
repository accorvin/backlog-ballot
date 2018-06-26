# backlog-ballot
A WebApp for uses to vote on issues to be prioritized from a JIRA backlog

# Steps for creating the project in OpenShift

  * First, login with the necessary `oc login` command

  * Create the project
    ```oc new-project backlog-ballot```

  * Create the database secret
    ```
    oc create secret generic backlog-ballot-secret \
    --from-literal=database-password=$(openssl rand -base64 21)
    ```

  * Upload the template
    ```oc create -f backlog-ballot-openshift-template.yml```

  * Apply the template
    ```oc process backlog-ballot-template | oc apply -f -```
