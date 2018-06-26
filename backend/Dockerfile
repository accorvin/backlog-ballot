FROM fedora
LABEL maintainer "Alex Corvin <acorvin@redhat.com>"

RUN dnf -y install gcc redhat-rpm-config python3-devel python-psycopg2 \
    && dnf clean all
RUN mkdir /backlog-ballot-backend
WORKDIR /backlog-ballot-backend
COPY requirements.txt /backlog-ballot-backend
RUN pip-3 install --no-cache-dir -r requirements.txt
COPY . /backlog-ballot-backend

EXPOSE 5000
CMD ./docker-entrypoint.sh
