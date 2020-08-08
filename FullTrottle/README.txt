# Design and implement a Django application with User and ActivityPeriod models
	
	
## Techniques
- Python3
- Django
- MongoDB
- Mongoengine

## Custom Management Command
 - python manage.py user_activity_command 5

## API's are listed below:

    - To get user data and activity periods of a user with the help of 'id':

        ```curl -X GET \
          'http://127.0.0.1:8000/full_throttle/get_user_detail_activity?id=xyz' \
          -H 'Postman-Token: a1ea5c30-c772-43a2-94be-41503e432c0d' \
          -H 'cache-control: no-cache'```
 
    - To get all the user data:
        
        ```curl -X GET \
          http://127.0.0.1:8000/full_throttle/get_all_users \
          -H 'Postman-Token: a760185e-c52e-462e-a0ee-7473fab33ede' \
          -H 'cache-control: no-cache'```

    - To create a user:

        ```curl -X POST \
          http://127.0.0.1:8000/full_throttle/create_user \
          -H 'Content-Type: application/json' \
          -H 'Postman-Token: a40e0876-a0a0-4433-9049-804069d96537' \
          -H 'cache-control: no-cache' \
          -d '{
	        "id":"xyz",
	        "real_name":"prince",
	        "tz":"Asia/Kolkata"
        }'```

    - To get a particular user data with 'id':
        
        ```curl -X GET \
          'http://127.0.0.1:8000/full_throttle/get_user?id=xyz' \
          -H 'Postman-Token: 14e2b45c-a57f-4011-a1b0-8bb957630bcd' \
          -H 'cache-control: no-cache'```

    - To create a partcular user activity period with 'id':

        ```curl -X POST \
          http://127.0.0.1:8000/full_throttle/create_user_activity \
          -H 'Content-Type: application/json' \
          -H 'Postman-Token: c09e1e0a-f338-4eda-896f-95084cd1ba09' \
          -H 'cache-control: no-cache' \
          -d '{
	        "id":"xyz",
	        "start_time":"jan 27 1am",
	        "end_time":"jan 27 7am"
        }'```

    - To get a particular user activity period with 'id':

        ```curl -X GET \
          'http://127.0.0.1:8000/full_throttle/get_user_activity?id=yy' \
          -H 'Postman-Token: 8837ecb5-2a37-4419-a506-687fb068ae4a' \
          -H 'cache-control: no-cache'```

    - To delete the user data and his activity periods with the help of 'id':

        ```curl -X DELETE \
          'http://127.0.0.1:8000/full_throttle/delete_user?id=VmLUH' \
          -H 'Postman-Token: e96ac31b-ab00-4305-b10c-3dada4f97979' \
          -H 'cache-control: no-cache'```
