import string


def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    in_sentence = []

    if sentence:
        if sentence == alphabet:

            return True

        else:
            for l in sentence.lower():
                if l not in alphabet:
                    continue
                elif len(in_sentence) >= 1 and l in in_sentence:
                    continue
                elif l in alphabet and l not in in_sentence:
                    in_sentence.append(l)

                    if len(in_sentence) == 26:

                        return True

                    else:
                        continue

                else:

                    return False

    else:

        return False
