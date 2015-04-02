from fabric.api import local

from settings import GAE_APP_ID


def db_download():
    local('rm data.dat')
    local('appcfg.py -A s~%s --url=http://%s.appspot.com/_ah/remote_api/ '
          '--filename data.dat download_data .' % (GAE_APP_ID, GAE_APP_ID))


def db_set():
    local(
        'appcfg.py -A dev~%s --url=http://localhost:8080/_ah/remote_api/ '
        '--filename=data.dat --email=foobar@nowhere.com upload_data .' % GAE_APP_ID)


def deploy():
    local('appcfg.py update ./')