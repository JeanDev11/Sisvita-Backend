import psycopg2

# Conectar a la base de datos
conn = psycopg2.connect(
    dbname="sisvita_g9", user="admin", password="75hvySMo6nfAzcupuKlnKMq44gKoBOCL", host="dpg-cp53stocmk4c73es9di0-a.oregon-postgres.render.com"
)
cursor = conn.cursor()

# Verificar la existencia de la columna 'fecha_nac'
cursor.execute("""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name='usuarios' AND column_name='fecha_nac';
""")
column = cursor.fetchone()

# Si la columna no existe, agregarla
if not column:
    print("no!")
else:
    print("si")
    
# Cerrar la conexión
cursor.close()
conn.close()
