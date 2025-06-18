git clone git@github.com:romanmikh/snowflakes.git snowflakes && cd snowflakes
python3 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pytest
python3 1
<!-- python3 2
python3 3 -->