text = "X-DSPAM-Confidence:    0.8475"
data = text.find("0.8475")
data1 = text[data:]

value = float(data1)
print(value)