import logging
import time


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def main():
    while True:
        logging.error('{"level":"info","name":"fred","home":"bedrock"}')
        time.sleep(5)

if __name__ == "__main__":
    main()
