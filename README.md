# Demo Discount Service

### Abstract
* ### The project aims at providing a discount code generating and distribution service, via implementation of several endpoints, for the brand to generate discount code and for the enduser to be able to easily obtain them. Future development of the project would require access to the user model of the registered user, item model describing each inventory item in the store, where granular control could be implemented on the level of the discounts codes. As this is a demo project written in about 3 to 4 hours or so there is a lot of room for improvement, and I am looking forward into analyzing the code with you, finding its flaws providing potential solutions and exploring the scaling potential. 
### Requirements
* #### docker
* #### docker-compose
* #### python3.9
### Project components
* #### Nginx Reverse Proxy
* #### Gunicorn - WSGI HTTP Server
* #### Discounts application
* #### PostGreSQL Database

### Project setup
* #### Clone the git repository
* #### Open api-app.env and database.env and populate them with your own usernames and password. Docker-compose will take values from those files when building containers. Alternatively you do not need to change anything and can run as is with the demo creds. The env files are a good way to prevent credentials from spilling into git repos (in this case I left generic credentials to reduce the amount of hassle for you)
* #### Build all the needed containers 
    ```
    docker-compose build
    ```
* #### Start all containers
    ```
    docker-compose up
    ```
* #### Make migration:
    ``` 
    docker-compose run web python manage.py makemigrations
    ```
* #### Run migrations
    ``` 
    docker-compose run web python manage.py migrate
    ```
* #### Create an admin user (you will be prompted for username and password)
    ```
    docker-compose run web python manage.py createsuperuser
    ```
* #### That is it you are good to go. The api should now be available:
    ```
    http://127.0.0.1:8001/discounts/generate-discount-tokens/
    ```
* #### It is running in DEBUG mode so accessing any unmapped paths or passing wrong parameters to requests will generate a debug report

## Endpoints
* ### ```/discounts/enerate-discount-tokens/```
  * METHOD: ```POST```
  * Params: 
    ```
    {
      "brand_name": "TEST_BRAND",
      "discount_percentage": "20",
      "number_of_codes": "10",
      "enabled": "1",
      "valid_from":"2022-04-11 07:29:33",
      "valid_to":"2022-04-11 07:29:33"
    }
    ```
  * Curl:
    ``` 
     curl -X POST -F 'brand_name=TEST_BRAND' -F 'discount_percentage=20' -F 'number_of_codes=2' -F 'enabled=1' -F 'valid_from=2022-04-11 07:29:33' -F 'valid_to=2023-04-11 07:29:33' http://127.0.0.1:8001/discounts/generate-discount-tokens/
    ```
* ### ```/discounts/update_discount/```
  * METHOD: ```PUT```
  * PARAMS:
    ```
    {
      "brand_name": "TEST_BRAND_2",
      "discount_percentage": "20",
      "number_of_codes": "10",
      "enabled": "1",
      "valid_from":"2022-04-11 07:29:33",
      "valid_to":"2022-04-11 07:29:33"
    }
    ```
  * Curl:
    ``` 
    curl -v -X PUT -F 'brand_name=TEST_BRAND_2' -F 'discount_percentage=20' -F 'number_of_codes=2' -F 'enabled=1' -F 'valid_from=2022-04-11 07:29:33' -F 'valid_to=2023-04-11 07:29:33' http://127.0.0.1:8001/discounts/update_discount/
    ```
* ### ```/discounts/get_discount/<brand_name>/<user_id>/```
  * METHOD ```GET```
  * Curl:
    ``` 
    curl -v -X GET http://127.0.0.1/discounts/get_discount/SOME_BRAND/68150717-4604-4603-906d-bbb325e25902/
    ```