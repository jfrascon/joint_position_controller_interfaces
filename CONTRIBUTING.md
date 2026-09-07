# Contributing

Treat changes to `JointPosition.action` as changes to a public ROS 2 contract.
Update the server, clients, documentation, and tests whenever an action field or its meaning changes.
Contributions are provided under the Apache License 2.0 used by this package.

## Development checks

Source the ROS 2 environment before running the hooks because the local `ament` hooks use tools from that environment.

Install the hooks once in each clone:

```bash
pre-commit install
```

Run every hook against the repository before requesting a review:

```bash
pre-commit run --all-files
```

Ruff applies safe fixes, formats Python, and sorts imports.
The `ament` hooks then validate Python, CMake, and XML using the ROS 2 tooling.
Both local hooks and package tests use `ament_flake8.ini` to enforce the 100-character limit and accept Ruff's slice spacing.

Run the package tests after changing the action contract or its validation:

```bash
colcon test --packages-select joint_position_controller_interfaces
colcon test-result --verbose
```
