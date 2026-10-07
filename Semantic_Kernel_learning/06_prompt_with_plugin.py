import asyncio
import os

from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from plugins.employee_plugin import EmployeePlugin


async def main():

    load_dotenv()

    kernel = Kernel()

    kernel.add_service(
        AzureChatCompletion(
            deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            endpoint=os.getenv("AZURE_OPENAI_BASE_URL"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY")
        )
    )

    kernel.add_plugin(
        EmployeePlugin(),
        plugin_name="Employee"
    )

    prompt = """
    The employee with ID {{$employee_id}} has the role:
    {{Employee.get_employee_role $employee_id}}

    Explain this information in one simple sentence.
    """

    employee_function = kernel.add_function(
        function_name="EmployeeRoleExplanation",
        plugin_name="EmployeeInfo",
        prompt=prompt
    )

    result = await kernel.invoke(
        employee_function,
        employee_id="EMP101"
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())