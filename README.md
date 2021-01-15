# StudentOwl-Monitoreo

## Commands

### Convert file.ui to file.py

```bash
pyuic5 .\resources\[file].ui -o .\views\[file].py
```

### Convert resources.qrc to resources.py

```bash
pyrcc5 .\resources\resource.qrc -o .\resources\resource_rc.py
```

### Run discover all test files

```bash
python -m unittest discover
```

### Peticiones GET
Realizar una peticion GET a un servidor
```python
import requests

r = requests.get('https://miapi.com/posts/')
posts = r.json()
```

### Peticiones POST
```python
import requests

payload = {'comentario': 'Está genial', 'estrellas': 5}
r = requests.post('https://miapi.com/comentarios/', json=payload)
```
