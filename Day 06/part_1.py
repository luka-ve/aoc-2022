test_result = 7


def main(input_file):
    message_length = 14

    with open(input_file, "r") as f:
        signal = f.read()

    for i in range(message_length, len(signal)):
        buffer = signal[i-message_length:i]

        if len(set(buffer)) == message_length:
            return i
