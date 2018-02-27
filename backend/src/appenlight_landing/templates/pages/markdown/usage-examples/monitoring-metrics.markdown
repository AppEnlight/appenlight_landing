Title: Monitor infrastructure or key metrics using the general metrics API

# Monitor infrastructure or key metrics using the general metrics API

!!! note "HINT"
    This example shows how to monitor a single server cpu usage, but this approach
    can also be used to **monitor custom metrics like in-application fraud attempts or
    daily sales** in a e-commerce platform.

    You can use our APIs by directly sending JSON - [metrics API](/page/api/0.5/general_metrics) and [log API](/page/api/0.5/logs).

AppEnlight allows you to send your data in a format that allows for charting.

Charts on other hand allow alert rules to be applied to them based on
values exceeding thresholds in specific timeframes.

Using a solution like the excellent **[python-diamond](http://diamond.readthedocs.org/en/latest/)**
 package + **[appenlight-diamond](https://pypi.python.org/pypi/appenlight-diamond)**
 for system metrics aggregation, you can build notification systems for
 various events that happen in your infrastructure/applications.

Once the data gets indexed in our logging or general metrics API, you can
create a graph based on the data.

<img src="/static/images/sections/pages/usage-examples/other/chart-servers-loadavg.png" alt="server usage" class="img-responsive">

One we have a working saved chart, then we can create an alert from its data.

The alert system checks all charts and applies a custom user created rule to every
interval range and value in the chart. If the rule matches, then a new
alert event is generated and sent out to the channels selected for the alert.

<img src="/static/images/sections/pages/usage-examples/other/chart-servers-loadavg-alert.png" alt="server usage" class="img-responsive">
