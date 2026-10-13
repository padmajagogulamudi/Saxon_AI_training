
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
    Hello {{name}}.

    You are {{role}}.
    """

    config = PromptTemplateConfig(
        name="BasicHandlebars",
        template=prompt,
        template_format="handlebars"
    )

    template = HandlebarsPromptTemplate(
        prompt_template_config=config
    )

    arguments = KernelArguments(
        name="Padmaja",
        role="Software Engineer"
    )

    rendered_prompt = await template.render(
        kernel,
        arguments
    )

    print(rendered_prompt)


if __name__ == "__main__":
    asyncio.run(main())

