# joint_position_controller_interfaces

This package contains the shared ROS 2 action definition used by the joint position controller server and by any client that talks to that server.

## Contents

- `action/JointPosition.action`

## What this package does

This package defines the action contract that both the joint position controller server and its clients must use.

It does not contain runtime nodes, launch files, or parameter files.

## Action contract

The goal contains one absolute joint position.
Positions use meters for prismatic joints and radians for revolute joints.
The server and client must therefore agree on the controlled joint type and unit.

The result reports whether the target was reached, the last measured position, and a human-readable terminal message.
The final position is `NaN` when the server cannot provide a valid measurement.
Feedback reports the requested target, the latest measured position, and their signed difference.
