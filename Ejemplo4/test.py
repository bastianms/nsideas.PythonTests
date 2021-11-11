from decouple import config

NOMBRE_SERVIDOR = config('SERVIDOR')

print(NOMBRE_SERVIDOR)