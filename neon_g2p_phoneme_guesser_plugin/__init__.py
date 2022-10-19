from ovos_plugin_manager.templates.g2p import Grapheme2PhonemePlugin, OutOfVocabulary
from phoneme_guesser import guess_phonemes


class PhonemeGuesserPlugin(Grapheme2PhonemePlugin):

    def get_arpa(self, word, lang, ignore_oov=False):
        lang = lang.lower()[:2]
        if lang == "en":
            return guess_phonemes(word, "en")
        if ignore_oov:
            return None
        raise OutOfVocabulary

    @property
    def available_languages(self):
        """Return languages supported by this G2P implementation in this state
        This property should be overridden by the derived class to advertise
        what languages that engine supports.
        Returns:
            set: supported languages
        """
        return {"en"}


# sample valid configurations per language
# "display_name" and "offline" provide metadata for UI
# "priority" is used to calculate position in selection dropdown
#       0 - top, 100-bottom
# all keys represent an example valid config for the plugin
PhonemeGuesserConfig = {
    "en-us": [
        {"lang": "en-us",
         "display_name": "Phoneme Guesser",
         "priority": 60,
         "native_alphabet": "ARPA",
         "durations": False,
         "offline": True}
    ]
}
