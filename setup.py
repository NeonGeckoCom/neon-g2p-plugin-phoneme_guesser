#!/usr/bin/env python3
from setuptools import setup


PLUGIN_ENTRY_POINT = 'neon-g2p-phoneme-guesser-plugin=neon_g2p_phoneme_guesser_plugin:PhonemeGuesserPlugin'
setup(
    name='neon-g2p-phoneme-guesser-plugin',
    version='0.0.1',
    description='A utterance2phoneme plugin ovos/neon/mycroft',
    url='https://github.com/NeonGeckoCom/g2p-phoneme-guesser-plugin',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='bsd3',
    packages=['neon_g2p_phoneme_guesser_plugin'],
    zip_safe=True,
    keywords='mycroft plugin utterance phoneme',
    entry_points={'ovos.plugin.g2p': PLUGIN_ENTRY_POINT}
)
