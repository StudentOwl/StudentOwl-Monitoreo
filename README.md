# StudentOwl-Monitoreo

## Commands

### Convert file.ui to file.py

```cmd
pyuic5 .\resources\[file].ui -o .\views\[file].py
```

### Convert resources.qrc to resources.py

```cmd
pyrcc5 .\resources\resource.qrc -o .\resources\resource_rc.py
```

### Run discover all test files

```cmd
python -m unittest discover
```
### Prueba