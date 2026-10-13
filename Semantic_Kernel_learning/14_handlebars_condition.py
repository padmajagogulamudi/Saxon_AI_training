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
Employee: {{name}}

{{#if is_admin}}
You have administrator access.
{{else}}
You have regular employee access.
{{/if}}
"""

    config = PromptTemplateConfig(
        name="EmployeeAccess",
        template=prompt,
        template_format="handlebars"
    )

    template = HandlebarsPromptTemplate(
        prompt_template_config=config,
        allow_dangerously_set_content=True
    )

    arguments = KernelArguments(
        name="Padmaja",
        is_admin=False
    )

    rendered_prompt = await template.render(
        kernel,
        arguments
    )

    print(rendered_prompt)


if __name__ == "__main__":
    asyncio.run(main())