curl -v -d '{"Action":0, "Mp3":1}' -H "Content-Type: application/json" -H "Authorization: X" -X POST localhost:8000/asd/MocManager

gunicorn apiManager:app

"/home/kechunet/Music/GUSTAVO CERATI -  Adios.mp3"