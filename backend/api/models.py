import uuid

from api import db


class Issue(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    vote_count = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, nullable=False)
    jira_issue_url = db.Column(db.Text, nullable=False)
    jira_key = db.Column(db.Text, nullable=False)

    def __init__(self, title, description, created, jira_issue_url, jira_key):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.vote_count = 0
        self.created = created
        self.jira_issue_url = jira_issue_url
        self.jira_key = jira_key

    def increment_votes(self):
        self.vote_count += 1

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'voteCount': self.vote_count,
            'jiraIssueUrl': self.jira_issue_url,
            'jiraKey': self.jira_key
        }
