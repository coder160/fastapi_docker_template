FROM python:3.9
WORKDIR /server
COPY ./requirements.txt /server/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt
COPY ./api_files /server/api_files
CMD ["uvicorn", "api_files.main:api_fn", "--host", "0.0.0.0", "--port", "9028"]