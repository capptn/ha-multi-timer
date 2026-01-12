FROM python:3.12-alpine
WORKDIR /app
COPY app /app
RUN pip install flask requests apscheduler
CMD ["sh", "/run.sh"]
