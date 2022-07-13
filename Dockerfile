FROM python:3.9

ENV PORT=8525

EXPOSE $PORT

WORKDIR /opensource_dashboard

COPY . .

RUN pip install -r requirements.txt

CMD ["sh", "setup.sh", "&&", "streamlit", "run", "app.py"]