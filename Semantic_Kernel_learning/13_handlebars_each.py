
import asyncio

from semantic_kernel import Kernel
from semantic_kernel.functions import KernelArguments
from semantic_kernel.prompt_template import (
    PromptTemplateConfig,
    HandlebarsPromptTemplate
)


async def main():

    kernel = Kernel()

    prompt = """
Employee List

{{#each employees}}
Name: {{name}}
Role: {{role}}

{{/each}}
"""

    config = PromptTemplateConfig(
        name="EmployeeList",
        template=prompt,
        template_format="handlebars"
    )

    template = HandlebarsPromptTemplate(
        prompt_template_config=config,
        allow_dangerously_set_content=True
    )

    employees = [
        {"name": "Padmaja", "role": "AI Intern"},
        {"name": "Akshaya", "role": "AI Intern"},
        {"name": "Rahul", "role": "Software Engineer"}
    ]

    arguments = KernelArguments(
        employees=employees
    )

    rendered_prompt = await template.render(
        kernel,
        arguments
    )

    print(rendered_prompt)


if __name__ == "__main__":
    asyncio.run(main())
