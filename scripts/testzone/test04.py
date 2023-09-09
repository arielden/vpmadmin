import uuid

def generate_uuid():
    return str(uuid.uuid4())

for i in range(20):
    vari = generate_uuid()
    print(vari)


