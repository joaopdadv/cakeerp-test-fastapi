from python3

copy .tests ./app
copy .requeriments.txt ./requeriments.txt

run pip install --no-cache-dir -r requeriments.txt

CMD["uvicorn","tests:api:app","--host","0.0.0.0","--port","80"]
