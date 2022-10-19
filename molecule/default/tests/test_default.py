"""tested python """
import os
import testinfra.utils.ansible_runner
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_python3_pip_is_installed(host):
    """pip is installed"""
    python3_pip = host.package("python3-pip")
    assert python3_pip.is_installed


def test_python3_setuptools_is_installed(host):
    """setuptools in installed"""
    python3_setuptools = host.package("python3-setuptools")
    assert python3_setuptools.is_installed


def test_python3_wheel_is_installed(host):
    """wheel is installed"""
    python3_wheel = host.package("python3-wheel")
    assert python3_wheel.is_installed


def test_python3(host):
    """python3 command"""
    assert host.find_command('python3')


def test_pip3(host):
    """pip3 command"""
    assert host.find_command('pip3')
