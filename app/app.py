import logging
import time


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def generate_large_string(size_mb):
    # 1 MB = 1024 * 1024 bytes
    one_mb = 1024 * 1024
    # Character to repeat to fill the string
    char_to_repeat = 'a'
    # Calculate how many times to repeat the character
    repeat_count = one_mb // len(char_to_repeat)
    # Generate the large string
    large_string = char_to_repeat * repeat_count
    return large_string

def main():
    size_mb = 1
    large_string = generate_large_string(size_mb)
    while True:
        logging.error(large_string)
        time.sleep(10)

if __name__ == "__main__":
    main()

