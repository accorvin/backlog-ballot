FROM python

RUN mkdir /issue-fetcher
WORKDIR /issue-fetcher
COPY requirements.txt /issue-fetcher/
RUN pip install -r requirements.txt
COPY . /issue-fetcher/

CMD python issue_fetcher.py
