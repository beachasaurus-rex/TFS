cd src
python -m venv .
. Scripts/activate
pip install numpy
pip freeze --local > requirements.txt

cd ../test
python -m venv .
. Scripts/activate
pip install -r ../src/requirements.txt
