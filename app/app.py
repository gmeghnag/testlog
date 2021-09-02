import logging
import time


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def main():
    while True:
        logging.error('ERROR: ocasalsa kernel: CPU4: Package temperature/speed high')
        time.sleep(5)

if __name__ == "__main__":
    main()