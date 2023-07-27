from setuptools import setup, find_packages

setup(
    name='Mailbox Validator',
    version='1.0.0',
    url='https://github.com/cc46808/mailbox-validator',
    author='Craig Carroll',
    author_email='craig@craigcarroll.design',
    description='A script to validate email addresses using the MailboxValidator API',
    packages=find_packages(),    
    install_requires=[
        'tqdm'
    ],
)
