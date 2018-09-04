import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize("name", [
    "lorem",
])
def test_rbenv_install(host, name):
    f = host.file("/home/{0}/.rbenv".format(name))

    assert f.exists
    assert f.is_directory
    assert f.user == name
    assert f.group == name


@pytest.mark.parametrize("name", [
    "lorem",
])
@pytest.mark.parametrize("plugin", [
    "rbenv-default-gems",
    "ruby-build",
])
def test_rbenv_plugin_install(host, name, plugin):
    f = host.file("/home/{0}/.rbenv/plugins/{1}".format(name, plugin))

    assert f.exists
    assert f.is_directory
    assert f.user == name
    assert f.group == name
