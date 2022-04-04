import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_check_repofile(host):
    repofile = host.file("/etc/yum.repos.d/fluentbit.repo")
    assert repofile.exists
    assert repofile.is_file
    assert repofile.user == 'root'
    assert repofile.mode == 0o644

def test_installation(host):
    assert host.package("fluent-bit").is_installed