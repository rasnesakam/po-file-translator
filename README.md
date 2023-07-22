# PO translator

PO translator is the bot that translates every entry that po file contains from google translate in Chrome browser

## Usage
### Activate virtual environment

Windows
```
Set-ExecutionPolicy Unrestricted -Scope Process # For windows 11
.\venv\Scripts\activate

```

Linux / Mac OS
```
source venv/Scripts/activate
```
### Install dependencies
```
pip install -r requirements.txt
```

### Run application
```
python main.py
```

### Enter inputs
```
Enter dir of po file: /dir/to/po/in
Enter dir of po output: /dir/to/po/out
```