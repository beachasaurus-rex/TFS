cd src
. Scripts/activate
pip freeze --local > requirements.txt

cd ../test
. Scripts/activate
pip install -r ../src/requirements.txt
