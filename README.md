## user transaction app

A user transaction application has been built using Python, JWT Token, Celery,
Django, Django rest framework, and drf_spectacular package for API docs. 
A user can send any amount from his/her balance to one or many other users 
at now or scheduled time. The user is also able to see the transaction history.


## Installation
```
# Python version 3.10.4
git clone https://github.com/shoumitro-cse/user_transaction_app.git
cd user_transaction_app
cp env.example .env
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
rm -rf static
mv staticfiles static
python manage.py runserver
```

## Celery for scheduled transaction
```
docker run --name redis_container -p 6379:6379 -d redis
celery -A user_transaction_app worker -l INFO
```

## API docs

```
Here, It has been used as a drf_spectacular package for API docs, I think that it will be 
very helpful for frontend developers. If you would like to see special instructions for 
each api, please keep your eye on each API doc.
protocol = http, https
domain = localhost or others
port = 80, 8000 etc
{protocol}://{domain}:{port}/api/docs/ (for API HTTP methods and descriptions)
{protocol}://{domain}:{port}/api/redocs/
{protocol}://{domain}:{port}/api/schema/ (for download API ymal file)
```
![](https://github.com/shoumitro-cse/user_transaction_app/blob/main/docs/api_doc_image.png?raw=true)

## Testing
```
Here, A total of 18 (Eighteen)  unit test case has been added. also, you can run it separately. 
Each testing class doc provides instructions on how to run it.
To run all test cases:
python manage.py test tests
```

![](https://github.com/shoumitro-cse/user_transaction_app/blob/main/docs/unit_testing_image.png?raw=true)


