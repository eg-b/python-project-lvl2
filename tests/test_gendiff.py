from gendiff.generate_diff import make_compare, generate_diff
from fixtures import content
import json, os

def test_relpath():
    assert generate_diff('fixtures/1.json', 'fixtures/2.json') == '{\n   host: hexlet.io\n - timeout: 50\n}'

def test_abspath():
    assert generate_diff(
        '/home/eg/python_projects/python-project-lvl2/fixtures/2.json',
        '/home/eg/python_projects/python-project-lvl2/fixtures/1.json'
    ) == '{\n   host: hexlet.io\n + timeout: 50\n}'


def test_both_path():
    assert generate_diff(
        'fixtures/2.json',
        '/home/eg/python_projects/python-project-lvl2/fixtures/1.json'
    ) == '{\n   host: hexlet.io\n + timeout: 50\n}'