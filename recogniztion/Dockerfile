FROM python:3.10.9
WORKDIR /app
copy requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "manage.py","runserver"]
COPY . .
EXPOSE 8000
CMD ['python','manage.py','runserver',"0.0.0.0:8000"]
