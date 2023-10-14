import logging
import concurrent.futures
import urllib.request
import tempfile
import shutil

links = [
        "http://python.org/",
        "https://www.python.org/about/",
        "https://www.python.org/community/"
    ]

def thread_function(link):
    logging.info("Thread %s: starting", link)
    with urllib.request.urlopen(link) as response:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp_file:
            shutil.copyfileobj(response, tmp_file)
            logging.info("Tmp file name is %s", tmp_file.name)
    logging.info("Thread %s: finishing", link)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")


    # Managing threads with ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, links)
