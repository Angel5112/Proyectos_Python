FROM python:3.8.10

WORKDIR /Vanilla_Projects
COPY requirements.txt /Vanilla_Projects/requirements.txt
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt
COPY . /Vanilla_Projects/

CMD bash -c "while true; do sleep 1; done"
