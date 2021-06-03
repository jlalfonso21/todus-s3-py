# Todus S3 Downloader

## Usage
- (Optional) create a virtualenv and activate it
```
$ python -m venv venv
$ source venv/bin/activate
```

- Install dependencies (recommended a virtualenv)
```
$ pip install -r requirements.txt
```

- Run script
```
$ python main.py /path/to/s3/links/file.txt -o /path/to/folder/to/download/files/
```
- Run Help
```
$ python main.py -h
```


## TODOs
- [ ] auth for S3 server
- [ ] process args from CLI
- [ ] pass a file location to load
- [ ] download files listed in the input file
- [ ] save files downloaded to custom location
