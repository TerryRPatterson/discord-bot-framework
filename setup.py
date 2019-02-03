import setuptools

with open("README", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
        name="discord_bot_framework-Terryp",
        version="0.0.1",
        author="Terry Patterson",
        author_email="Terryp@wegrok.net",
        description="An expansion of discord.py.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/TerryRPatterson/discord_bot_framework",
        packages=setuptools.find_packages(),
        licence="Apache-2.0",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Topic :: Communications :: Chat",
            "Intended Audience :: Developers",
            "Framework :: AsyncIO",
            "Topic :: Software Development :: Libraries",
        ],
    )
