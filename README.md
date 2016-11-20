# Ansible Role `rbenv`

This is a basic Ansible role to install and enable [`rbenv`](https://github.com/rbenv/rbenv) on Ubuntu. It should also work on macOS. It performs the following tasks:

- Install rbenv.
- Add rbenv to path.
- (Optionally) install [`ruby-build`](https://github.com/rbenv/ruby-build) as an `rbenv` plugin.

## Variables

| Variable name | Default value | Description |
|---------------|---------------|-------------|
| `rbenv_users` | `[]`          | An array of users who need `rbenv` installed. Each item should include `user` and `group`.
| `rbenv_users_home_path_prefix` | `/home` | Path (from `/`) to the parent directory containing users on the system (should be identical to `$HOME`, and should not include a trailing slash). Default value works on macOS. |
| `use_rbenv_extension` | `True` | Whether or not "to compile dynamic bash extension to speed up rbenv." |
| `rbenv_profile_file` | `.bashrc` | Name of profile file to use when adding `rbenv` to path (e.g. `.bash_profile`, `.bashrc`, `.zshrc` etc). |
| `rbenv_export_line` | ` 'export PATH="$HOME/.rbenv/bin:$PATH"'` | The line to add to the profile file above to add rbenv to path. |
| `install_ruby_build` | `True` | Whether or not to install [`ruby-build`](https://github.com/rbenv/ruby-build) as an `rbenv` plugin. | 

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
    - ansible-role-rbenv
  vars:
    rbenv_users_home_path_prefix: "/home"
    rbenv_users:
      - {
        user: "ctorgalson",
        group: "ctorgalson"
      }
    rbenv_profile_file: ".zshrc"
```

## License

MIT
