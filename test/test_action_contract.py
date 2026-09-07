from joint_position_controller_interfaces.action import JointPosition


def test_joint_position_action_fields_are_stable() -> None:
    assert JointPosition.Goal.get_fields_and_field_types() == {'position': 'double'}
    assert JointPosition.Result.get_fields_and_field_types() == {
        'success': 'boolean',
        'final_position': 'double',
        'message': 'string',
    }
    assert JointPosition.Feedback.get_fields_and_field_types() == {
        'target_position': 'double',
        'current_position': 'double',
        'position_error': 'double',
    }
