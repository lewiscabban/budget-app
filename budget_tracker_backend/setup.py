from setuptools import setup

setup(
    name='budget_tracker_backend',
    version='0.1.0',
    description='Budget Tracker Backend',
    author='Lewis Cabban',
    author_email='lcabban@gmail.com',
    packages=['budget_tracker_backend'],
    install_requires=[
        'fastapi',
        'uvicorn[standard]',
        'strawberry-graphql[debug-server]',
        'pytest',
        'asyncio',
        'pytest-asyncio',
    ],
)
