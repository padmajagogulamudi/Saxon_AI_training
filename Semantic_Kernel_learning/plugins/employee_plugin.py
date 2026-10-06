
from semantic_kernel.functions import kernel_function


class EmployeePlugin:

    @kernel_function(
        name="get_employee_name",
        description="Get the employee name using employee ID."
    )
    def get_employee_name(self, employee_id: str) -> str:
        return "Padmaja"

    @kernel_function(
        name="get_employee_role",
        description="Get the employee role using employee ID."
    )
    def get_employee_role(self, employee_id: str) -> str:
        return "Software Engineer"
