from setuptools import setup

setup(
    name="kvuilder",
    version="1.0.0",
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
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Desktop Environment",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries"
    ],
    keywords="kivy kivymd gui android ios desktop application",
)