import traceback

from api import db
from api.models import Issue
from api.issues import bp
from flask import current_app, jsonify, request


def _get_all_issues(page=1, issues_per_page=15):
    issues = Issue.query.order_by(Issue.created.desc())
    paginate_issues = issues.paginate(page, issues_per_page, False)
    issues = [i.serialize for i in paginate_issues.items]
    return issues


@bp.route('/exists', methods=['POST'])
def issue_exists():
    post_data = request.get_json()
    required_keys = [
        'jiraKey'
    ]

    for key in required_keys.copy():
        if key in post_data:
            required_keys.remove(key)
    if len(required_keys) > 0:
        msg = ('The following required keys about the issue were not '
               'specified: {missing}').format(missing=required_keys)
        response = {
            'code': 'data_missing',
            'description': msg
        }
        return jsonify(response), 400

    jira_key = post_data['jiraKey']
    exists = Issue.query.filter_by(jira_key=jira_key).count() > 0
    if exists:
        msg = 'Issue with key {key} already exists'
        current_app.logger.debug(msg.format(key=jira_key))
    else:
        msg = 'Issue with key {key} does not exist'
        current_app.logger.debug(msg.format(key=jira_key))

    response = {'exists': exists}
    return jsonify(response), 200


@bp.route('/all', methods=['GET'])
def get_all_issues():
    page = request.args.get('page', 1, type=int)
    issues_per_page = request.args.get('issues_per_page', 20, type=int)
    msg = 'Attempting to get issues'
    current_app.logger.info(msg)
    try:
        issues = Issue.query.order_by(Issue.created.desc())
    except Exception:
        msg = 'Error while getting issues: {exc}'
        current_app.logger.error(msg.format(exc=traceback.format_exc()))
        response_object = {
            'code': 'fail',
            'message': msg.format(exc=traceback.format_exc())
        }
        return jsonify(response_object), 500
    current_app.logger.info('Successfully fetched issues')

    paginate_issues = issues.paginate(page, issues_per_page, False)
    issues = [i.serialize for i in paginate_issues.items]
    response_object = {
        'issues': issues
    }
    return jsonify(response_object), 200


@bp.route('/vote', methods=['POST', 'OPTIONS'])
def vote():
    if request.method != 'POST':
        response = {}
        return jsonify(response), 200

    post_data = request.get_json()
    if request.method == 'POST' and post_data is None:
        current_app.logger.error('Throwing error')
        response = {
            'code': 'no_data',
            'message': 'No post data was supplied'
        }
        return jsonify(response), 400

    required_keys = [
        'issueId'
    ]

    current_app.logger.debug(post_data)
    for key in required_keys.copy():
        if key in post_data:
            required_keys.remove(key)
    if len(required_keys) > 0:
        msg = ('The following required keys about the issue were not '
               'specified: {missing}').format(missing=required_keys)
        response = {
            'code': 'data_missing',
            'description': msg
        }
        return jsonify(response), 400

    issue_id = post_data['issueId']
    issue = Issue.query.filter(Issue.id == issue_id)[0]
    current_app.logger.debug('Incrementing vote on issue {0}'.format(issue))
    issue.increment_votes()
    db.session.add(issue)
    db.session.commit()
    current_app.logger.debug('Successfully incremented vote')

    issues = _get_all_issues()
    response = {'issues': issues}
    return jsonify(response), 201


@bp.route('/new', methods=['POST'])
def add_issue():
    # get the post data
    post_data = request.get_json()
    required_keys = [
        'title',
        'description',
        'created',
        'jira_issue_url',
        'jira_key'
    ]

    for key in required_keys.copy():
        if key in post_data:
            required_keys.remove(key)
    if len(required_keys) > 0:
        msg = ('The following required keys about the issue were not '
               'specified: {missing}').format(missing=required_keys)
        response = {
            'code': 'data_missing',
            'description': msg
        }
        return jsonify(response), 400

    title = post_data['title']
    description = post_data['description']
    created = post_data['created']
    jira_issue_url = post_data['jira_issue_url']
    jira_key = post_data['jira_key']

    # store issue
    issue = Issue(
        title=title,
        description=description,
        created=created,
        jira_issue_url=jira_issue_url,
        jira_key=jira_key
    )

    db.session.add(issue)
    db.session.commit()
    msg = 'Successfully saved a new issue'
    current_app.logger.info(msg)

    response_object = {
        'code': 'success',
        'description': 'Issue stored successfully'
    }
    return jsonify(response_object), 201
