from phoneme_guesser_plugin import PhonemeGuesserPlugin

print(PhonemeGuesserPlugin().guess_arpa_word("andromeda", "en"))
print(PhonemeGuesserPlugin().guess_ipa_word("andromeda", "en"))
print(PhonemeGuesserPlugin().guess_arpa("hey mycroft", "en"))
