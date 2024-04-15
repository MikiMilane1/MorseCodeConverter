dict_morse = {'A': '.-',
              'B': '-...',
              'C': '-.-.',
              'D': '-..',
              'E': '.',
              'F': '..-.',
              'G': '--.',
              'H': '....',
              'I': '..',
              'J': '.---',
              'K': '-.-',
              'L': '.-..',
              'M': '--',
              'N': '-.',
              'O': '---',
              'P': '.--.',
              'Q': '--.-',
              'R': '.-.',
              'S': '...',
              'T': '-',
              'U': '..-',
              'V': '...-',
              'W': '.--',
              'X': '--..--',
              'Y': '-.--',
              'Z': '--..',
              }

tuples_morse = []
keys = list(dict_morse.keys())
for n in range(len(keys)):
    tuples_morse.append((keys[n], dict_morse[keys[n]]))

