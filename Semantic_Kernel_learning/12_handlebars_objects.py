import asyncio

from semantic_kernel import Kernel
from semantic_kernel.functions import KernelArguments
from semantic_kernel.prompt_template import (
    PromptTemplateConfig,
    HandlebarsPromptTemplate
)
from semantic_kernel.prompt_template.input_variable import InputVariable


async def main():

    kernel = Kernel()

    prompt = """
    Employee Details

    Name: {{employee.name}}
    Role: {{employee.role}}
    Technology: {{employee.technology}}
    """

    config = PromptTemplateConfig(
        name="EmployeeDetails",
        template=prompt,
        template_format="handlebars",
        input_variables=[
            InputVariable(
                name="employee",
                allow_dangerously_set_content=True
            )
        ]
    )

    template = HandlebarsPromptTemplate(
        prompt_template_config=config
    )

    employee = {
        "name": "Padmaja",
        "role": "AI Intern",
        "technology": "Semantic Kernel"
    }

    arguments = KernelArguments(
        employee=employee
    )

    rendered_prompt = await template.render(
        kernel,
        arguments
    )

    print(rendered_prompt)


if __name__ == "__main__":
    asyncio.run(main())