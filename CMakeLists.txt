cmake_minimum_required(VERSION 3.8)
project(joint_position_controller_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME} "action/JointPosition.action")

install(FILES README.md LICENSE CONTRIBUTING.md
        DESTINATION share/${PROJECT_NAME})

ament_export_dependencies(rosidl_default_runtime)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)

  # Exclude linters that require package-specific configuration.
  list(APPEND AMENT_LINT_AUTO_EXCLUDE
    ament_cmake_flake8)

  # Register the remaining linters declared as test dependencies in package.xml.
  ament_lint_auto_find_test_dependencies()

  find_package(ament_cmake_flake8 REQUIRED)

  ament_flake8(CONFIG_FILE "${CMAKE_CURRENT_SOURCE_DIR}/ament_flake8.ini")

  ament_add_pytest_test(test_action_contract test/test_action_contract.py)
endif()

ament_package()
