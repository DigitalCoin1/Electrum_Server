from setuptools import setup

setup(
    name="electrum-sperocoin-server",
    version="0.9",
    scripts=['run_electrum_sperocoin_server','electrum-sperocoin-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumsperocoinserver':'src'
        },
    py_modules=[
        'electrumsperocoinserver.__init__',
        'electrumsperocoinserver.utils',
        'electrumsperocoinserver.storage',
        'electrumsperocoinserver.deserialize',
        'electrumsperocoinserver.networks',
        'electrumsperocoinserver.blockchain_processor',
        'electrumsperocoinserver.server_processor',
        'electrumsperocoinserver.processor',
        'electrumsperocoinserver.version',
        'electrumsperocoinserver.ircthread',
        'electrumsperocoinserver.stratum_tcp',
        'electrumsperocoinserver.stratum_http'
    ],
    description="SperoCoin Electrum Server",
    author="SperoCoin Developers",
    author_email="helper@sperocoin.org",
    license="GNU Affero GPLv3",
    url="https://github.com/DigitalCoin1/Electrum_Server/",
    long_description="""Server for the Electrum Lightweight SperoCoin Wallet"""
)


