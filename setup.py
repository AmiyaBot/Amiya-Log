import setuptools

with open('README.md', mode='r', encoding='utf-8') as md:
    description = md.read()

with open('requirements.txt', mode='r', encoding='utf-8') as req:
    requirements = sorted(req.read().lower().strip('\n').split('\n'))

with open('requirements.txt', mode='w', encoding='utf-8') as req:
    req.write('\n'.join(requirements))

setuptools.setup(
    name='amiyalog',
    version='0.1.0',
    author='vivien8261',
    author_email='826197021@qq.com',
    url='https://www.amiyabot.com/develop/advanced/logger.html',
    license='MIT Licence',
    description='AmiyaBot 日志模块',
    long_description=description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(include=['amiyalog', 'amiyalog.*']),
    include_package_data=True,
    python_requires='>=3.10',
    install_requires=requirements,
)

# python setup.py bdist_wheel
# twine upload dist/*
