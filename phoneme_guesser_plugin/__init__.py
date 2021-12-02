from ovos_plugin_manager.templates.phonemes import Grapheme2PhonemePlugin
from phoneme_guesser import guess_phonemes


class PhonemeGuesserPlugin(Grapheme2PhonemePlugin):

    def get_arpa(self, word, lang):
        lang = lang.lower()[:2]
        if lang == "en":
            return guess_phonemes(word, "en")
        return None


