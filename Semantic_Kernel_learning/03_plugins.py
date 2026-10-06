from semantic_kernel import Kernel
from plugins.employee_plugin import EmployeePlugin


kernel = Kernel()

employee_plugin = kernel.add_plugin(
    EmployeePlugin(),
    plugin_name="EmployeePlugin"
)

print("Employee plugin added successfully!")