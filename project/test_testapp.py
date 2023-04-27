import pytest

import testapp as app

@pytest.fixture(params=['nodict', 'dict'])
def generate_initial_transform_parameters(request, mocker):
    test_input = {
        'name': 'John Q. Public',
        'street': '123 Main St.',
        'city': 'Anytown',
        'state': 'FL',
        'zip': 99999,
    }
    expected_output = {
        'name': 'John Q. Public',
        'street': '123 Main St.',
        'city': 'Anytown',
        'state': 'FL',
        'zip': 99999,
    }

    if request.param == dict:
        test_input['relationships'] = {
            'siblings': ['Michael R. Public', 'Suzy Q. Public'],
            'parents': ['John Q. Public Sr.', 'Mary S. Public'],
        }

        expected_output['siblings'] = ['Michael R. Public', 'Suzy Q. Public']
        expected_output['parents'] = ['John Q. Public Sr.', 'Mary S. Public']

    mocker.patch.object(outside_module, 'do_something')
    mocker.do_something.return_value(1)
    mocker.do_something.side_effect([1,2])

    return test_input, expected_output

def test_initial_transform(generate_initial_transform_parameters):
    input_dict = generate_initial_transform_parameters[0]
    expected_output = generate_initial_transform_parameters[1]

    assert app.initial_transform(input_dict) == expected_output