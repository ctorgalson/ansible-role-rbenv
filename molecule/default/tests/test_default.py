import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("user", [
    "lorem",
    "ipsum",
])
def test_rbenv_install(host, user):
    f = host.file("/home/{0}/.rbenv".format(user))

    assert f.exists
    assert f.is_directory
    assert f.user == user
    assert f.group == user


@pytest.mark.parametrize("user", [
    "lorem",
    "ipsum",
])
@pytest.mark.parametrize("plugin", [
    "rbenv-default-gems",
    "ruby-build",
])
def test_rbenv_plugin_install(host, user, plugin):
    f = host.file("/home/{0}/.rbenv/plugins/{1}".format(user, plugin))

    assert f.exists
    assert f.is_directory
    assert f.user == user
    assert f.group == user


@pytest.mark.parametrize("user", [
    "lorem",
])
@pytest.mark.parametrize("line", [
    "export PATH=\"$HOME/.rbenv/bin:$PATH\"",
    "eval \"$(rbenv init -)\"",
])
def test_rbenv_bash_setup(host, user, line):
    f = host.file("/home/{0}/.bashrc".format(user))

    assert f.exists
    assert f.user == user
    assert f.group == user
    assert line in f.content_string


@pytest.mark.parametrize("user", [
    "ipsum",
])
@pytest.mark.parametrize("line", [
    "status --is-interactive; and source (rbenv init -|psub)",
])
def test_rbenv_fish_setup(host, user, line):
    f = host.file("/home/{0}/.config/fish/config.fish".format(user))

    assert f.exists
    assert f.user == user
    assert f.group == user
    assert line in f.content_string


""" todo: we should be testing rbenv commands as local users, but we can't
because testinfra uses `sudo -u lorem /bin/sh -c 'rbenv versions'` so the
bash/zsh/fish rc files aren't loaded, and everything blows up. """
