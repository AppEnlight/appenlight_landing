Title: Celery task monitoring

# Celery task monitoring

Approx. integration time: **5 minutes**

You can track exceptions in your Celery tasks.

## Installation and Setup

Install the `appenlight_client` using pip:

    pip install appenlight-client

-----

!!! note "Including frame local variables"
    In many cases, while integrating celery tasks you may want to see the
    contents of frame variables. You can set that in `APPENLIGHT_INI` or add
    `environ["appenlight.report_local_vars"] = 1` to the `fake_environ` object.

Modify your tasks file to contain an example configuration and client:

    ::python

    import appenlight_client.client as e_client
    from appenlight_client.ext.celery import register_signals
    
    CONFIG = e_client.get_config({'appenlight.api_key':'YOUR_PRIVATE_KEY'})
    APPENLIGHT_CLIENT = e_client.Client(CONFIG)
    register_signals(APPENLIGHT_CLIENT)


Run celeryd providing the **APPENLIGHT_INI** environment variable:

    APPENLIGHT_INI=/path/to/appenlight.ini celery worker

In some cases you might want to get notified every time you retry your task.
Celery version < 3.0 doesn't support `retry signal` and retried tasks are `NOT FAILED`.
so the `task_failure` signal will not get issued:

    ::python

    from appenlight_client.ext.general import gather_data

    @task(default_retry_delay=60, max_retries=24)
    def example_task(sometask_arg):
        try:
        .... your task code ....
        except Exception, exc:
            # fake environ object currently needed for client to operate 
            # this sends exception even if you want to retry it later
            fake_environ = {'appenlight.view_name':'celery:tasks.example_task'}
            gather_data(APPENLIGHT_CLIENT, fake_environ)
            example_task.retry(exc=exc)