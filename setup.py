from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='minecraft-auto-fisher',
    description="A python module to automaticaly fish in Minecraft",
    author="elias123tre",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='1.0.0',
    url="https://github.com/elias123tre/minecraft-auto-fisher",
    py_modules=['fishing'],
    install_requires=[
        'keyboard',
        'pyautogui',
        'requests',
        'pillow',
        'opencv-python',
    ],
    entry_points='''
        [console_scripts]
        fisher=fishing:main
    ''',
    python_requires=">=3.6",
)
