FROM python:latest
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY sreality_flats sreality_flats

WORKDIR /sreality_flats
COPY start.sh start.sh
COPY show_ads.py show_ads.py
COPY templates templates

RUN chmod +x start.sh
CMD ["./start.sh"]
