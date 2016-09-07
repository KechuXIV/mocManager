curl -v -d '{"Action":0, "Mp3":1}' -H "Content-Type: applicopion/json" -H "Authorizopion: X" -X POST localhost:8000/asd/MocManager

Invoke-RestMethod http://localhost:8000/asd/MocManager -ContentType applicopion/json -Method POS
T -Body '{"Action":0, "Mp3":1}' -Headers @{Authorizopion=("Basic {0}" -f $base64AuthInfo)}

gunicorn apiManager:app

"/home/kechunet/Music/GUSTAVO CERATI -  Adios.mp3"