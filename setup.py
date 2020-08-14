from setuptools import setup

with open("requirements.txt") as fp:
    install_requires = fp.read().splitlines() 

with open("README.md") as fp:
    LONG_DESCRIPTION = fp.read()

setup(
    name="kvuilder",
    version="1.0.1",
    license="MIT",
    platforms="any",
    packages=["kvuilder"],
    package_data={
        'kvuilder': ['data/*']
    },
    include_package_data=True,
    author="Aprila Hijriyan",
    author_email="hijriyan23@gmail.com",
    url="https://github.com/aprilahijriyan/kvuilder",
    description="Kivy Project Template Builder",
    long_description=LONG_DESCRIPTION,
    install_requires=install_requires,
    long_description_content_type='text/markdown',
    entry_points={
        "console_scripts": [
            "kvuilder=kvuilder.command:project_group"
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Natural Language :: Indonesian",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Desktop Environment",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries"
    ],
    zip_safe=False,
    python_requires='>=3.6',
    keywords="kivy kivymd gui android ios desktop application",
)