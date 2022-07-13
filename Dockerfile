FROM python:3.9

ENV PORT=8511

EXPOSE $PORT

WORKDIR /opensource_dashboard

COPY . .

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]