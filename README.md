# Windows RPC Interface Database

A simple database of Windows RPC interfaces, by <a href="https://github.com/jcspencer">James Spencer</a>

Contains excerpts from the [Microsoft Open Specifications](https://learn.microsoft.com/en-us/openspecs/main/ms-openspeclp/3589baea-5b22-48f2-9d43-f5bea4960ddb) website; all rights reserved.

## Development

'Protocols' (e.g. RPC protocols) are tied to 'services' (Windows Features, Roles, etc.)

- `services.py` contains a list of services
- `protocols.py` contains a list of protocols

To build the site:
- `build_database.py` builds the `database.json` file
- `build_page.py` renders the page from the template.