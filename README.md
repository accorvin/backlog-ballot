# backlog-ballot

A WebApp that allows users to vote on issues to be prioritized from a JIRA backlog

# Running locally

The easiest way to run the application locally is via docker-compose.
Simply run the command `docker-compose up -d` from the repo root.
The frontend will be available at http://localhost:4200

# Steps for deploying the tool in OpenShift

  * First, login with the necessary `oc login` command

  * Create the project
    ```
    oc new-project backlog-ballot
    ```

  * Create the database secret
    ```
    oc create secret generic backlog-ballot-secret \
    --from-literal=database-password=$(openssl rand -base64 21)
    ```

  * Upload the template
    ```
    oc create -f backlog-ballot-openshift-template.yml
    ```

  * Define your parameters

    Specify the necessary openshift parameters for your deployment. An example
    can be found in `open.paas.params.env`

  * Modify `frontend/src/environments/environment.prod.ts` so that the
    `api` variable points to `${BACKEND_ROUTE}/api/`. This shouldn't be
    necessary, as the value should get taken from the templated configmap,
    but I wasn't able to get this working correctly.

  * Apply the template
    ```
    oc process backlog-ballot-template --param-file=$PARAM_FILE | oc apply -f -
    ```
