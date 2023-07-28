message  = "Hello"

def get_frequency(text, word):
    words = text.split(" ")
    count = text.count("word")

    frequency = count / len(words) * 100
    return frequency

frequency = get_frequency("I love sun", "love")

if frequency >5:
    print("High Frequncy")

else:
    print("Low")

print(message)