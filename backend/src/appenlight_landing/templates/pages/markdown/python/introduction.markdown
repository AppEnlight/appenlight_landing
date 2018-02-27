Title: AppEnlight Python Client

# AppEnlight Python Client

The AppEnlight Python client is officially maintained by the AppEnlight team and uses
all of the functionality provided by our service.

**Supports all popular python frameworks including `Django`, `Pyramid`, `Flask` and others**

Install `appenlight_client` using pip:

    pip install appenlight-client

The client gathers and gives you detailed debugging and profile
information in the AppEnlight dashboard, including:

* **5 minute integration** with live application
* Supports report/log batching (with no negative effects on application performance)
* **Exceptions** including **frame local vars** (configurable per request)
* 404 requests
* **Python logging framework entries**
* Response times
* Apdex score
* Throughput (requests per minute)
* Performance metrics
* **Performance details of slow requests including slow calls/queries made by popular libraries**

Current out-of-the-box timing of the following libraries is supported:

* **Resource fetching** : `requests`, `urllib`, `urllib2`, `urllib3`, `httplib`
* **NoSQL** : `pysolr`, `python-memcached`, `redis`, `mongodb`
* **SQL** : most commonly used dbapi2 drivers (`mysql-python`, `psycopg2`, `odbc`, and many others)
* **Templates** : `django`, `jinja2`, `mako`

**[Client source on Github](https://github.com/AppEnlight/appenlight-client-python)**
