import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def get_os_name():
    with open('/etc/lsb-release', 'r') as lsb_release:
        for line in lsb_release.readlines():
            if line.startswith('DISTRIB_ID'):
                name = line.split('')[-1]
                return name

def test_check_repofile(host):
    if host.system_info.distribution == 'centos':
        repofile = host.file("/etc/yum.repos.d/fluentbit.repo")
    elif host.system_info.distribution == 'ubuntu':
        repofile = host.file(f"/etc/apt/sources.list.d/packages_fluentbit_io_ubuntu_{host.system_info.codename}.list")
    assert repofile.exists
    assert repofile.is_file
    assert repofile.user == 'root'
    assert repofile.group == 'root'
    assert repofile.mode == 0o644

def test_installation(host):
    assert host.package("fluent-bit").is_installed

def test_config_file(host):
    config = host.file("/etc/fluent-bit/fluent-bit.conf")
    assert config.exists
    assert config.is_file
    assert config.user == 'root'
    assert config.group == 'root'
    assert config.mode == 0o644

def test_service(host):
    fluent_bit = host.service("fluent-bit")
    assert fluent_bit.is_running
    assert fluent_bit.is_enabled

def test_socket(host):
    assert host.socket("tcp://0.0.0.0:24224").is_listening
    assert host.socket("tcp://0.0.0.0:2020").is_listening