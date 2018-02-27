Title: Report grouping

# Report grouping

AppEnlight groups reports together in an intelligent manner.
When reports are grouped, instead of a new entry, `report details` are *appended*
to existing report, and the `occurences` counter is increased. Please note that new entries
are never appended to reports `marked as fixed`; a new fresh report will be created
instead.

Default grouping behaviour can be configured on a per-application basis using the
app settings section.

However, we are aware that sometimes this might not be enough in specific cases.
You can send a special field in reports called `group_string` that will be
hashed on our end and will be used as a base for grouping - this allows you to
override the default behavior and set your own rules for grouping reports.

Related links:

**[Information on grouping control with a python client](/page/python/client-configuration#tips-tricks)**
