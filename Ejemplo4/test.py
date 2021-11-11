from decouple import config

NOMBRE_SERVIDOR = config('SERVIDOR_DB')

print(NOMBRE_SERVIDOR)