# pyophase

pyophase is our management application used for organizing an introductory week for new students. Such an introductory week is called Ophase.

## Development

Please keep the following things in mind:
* Objects which are relevant for only one Ophase should have a foreign key referring to this Ophase. This allows deleting all data associated to a specific Ophase by removing this single object.
* Create and commit migrations after the database scheme changed (e.g. model changes). `./manage.py makemigrations`
* Recreate, (maybe translate) and commit message files after a string is introduced or changed. `cd changed-app && ../manage.py makemessages`
* From time to time, look for new versions of the dependencies, listed in `requirements.txt` and `bower.json`, test them and commit updated files.
* When new major functionality is introduced, briefly explain it in `DOCUMENTATION.md`.

## Deployment

### Installation
* Install `python3`, `python3-pip`, `python3-virtualenv` and `bower` (the latter maybe via `npm`)
* Maybe create a user for Django/WSGI applications (e.g. `django`)
* Clone this repository into a proper directory (e.g. `/srv/pyophase`)
* Maybe create MySQL database and proper user
* Create the file `pyophase/settings_local.py` and fill it with production settings (it will be imported by `settings.py` and overrides default settings)
* Create a virtualenv (e.g. `virtualenv -p python3 venv`)
* For serving WSGI applications, one can install `uwsgi`, create an ini file under `/etc/uwsgi/` with the proper configuration and configure the webserver to use mod-proxy-uwsgi to make the application accessible. The webserver should also serve the static files.
* Run all the relevant commands from the Updates section

### Updates

* `systemctl stop uwsgi`
* `git pull`
* `bower install` when the `bower.json` file changed
* `source venv/bin/activate` when one of the `pip` or `./manage.py` steps are necessary
* `pip install -r requirements.txt` when the `requirements.txt` file changed
* `./manage.py migrate` when a new migrations file is available
* `./manage.py collectstatic` when a static file changed (or `bower install` was run)
* `./manage.py compilemessages` when a message file (`*.po`) changed
* `deactivate` when virtualenv was activated
* `chown -R django:django .`
* `systemctl start uwsgi`

## Usage

A documentation (in German) for users of pyophase is available in `DOCUMENTATION.md`.

## Data Privacy

During the organizational work, it is unavoidable to store certain data, some of which is related to individual persons. pyophase is designed in a way such that it is easy to delete all the data after it is no longer needed. The head of Ophase is told to delete this data as early as possible.

## License

Files in pyophase are licensed under the Affero General Public License version 3, the text of which can be found in `LICENSE-AGPL.txt`, or any later version of the AGPL, unless otherwise noted.
