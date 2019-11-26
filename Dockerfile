
FROM python:3.7

WORKDIR /home/traun/DB_UI

COPY requirements.txt /home/traun/DB_UI/requirements.txt
RUN apt-get install libgl1-mesa-glx
RUN pip install -r requirements.txt

RUN pip uninstall bson --yes
RUN pip uninstall pymongo --yes
RUN pip install pymongo --user

COPY . .
EXPOSE 80

CMD [ "python", "./Main.py" ]
