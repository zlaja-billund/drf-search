# Django Rest Framework API Search Filter

## 1. Overview
This project demonstrates how to add search and filtering functionality to a Django Rest Framework (DRF) API using `django-filter`.  
It includes a simple model, serializer, viewset, and URL configuration to illustrate how filters can be integrated into an API endpoint.


## 2. Requiremnts
- asgiref==3.9.1
- Django==5.2.5
- django-filter==25.1
- djangorestframework==3.16.1
- Markdown==3.9
- sqlparse==0.5.3

## 3. Installation
1. Clone this repository:
   ```bash
   git clone git@github.com:zlaja-billund/drf-search.git
   cd drf-search-filter-example

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
   
3. Install dependencies:
    ``` bash
    pip install -r requirements.txt
   
4. Run migrations
    ``` bash
   python manage.py migrate
   
## 4. License & Author
### License
This project is licensed under the MIT License.

### Author
Developed by Zlaja (https://github.com/zlaja-billund)
