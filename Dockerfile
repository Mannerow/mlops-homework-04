FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["score.py", "./"]

ENTRYPOINT ["python", "score.py"]
#provides command line args as defaults that can be overridden
CMD ["2023", "4"]