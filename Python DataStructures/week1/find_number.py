text = "X-DSPAM-Confidence:    0.8475"
number=text.find('0')
print(float(text[number:]))
