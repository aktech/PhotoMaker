import subprocess
import time


SAFETY_CACHE = "./models/safety-cache"
SAFETY_URL = "https://weights.replicate.delivery/default/sdxl/safety-1.0.tar"

BASE_MODEL_URL = "https://weights.replicate.delivery/default/SG161222--RealVisXL_V3.0-11ee564ebf4bd96d90ed5d473cb8e7f2e6450bcf.tar"
BASE_MODEL_PATH = "models/SG161222/RealVisXL_V3.0"

PHOTOMAKER_URL = "https://weights.replicate.delivery/default/TencentARC--PhotoMaker/photomaker-v1.bin"
PHOTOMAKER_PATH = "models/photomaker-v1.bin"

def download_weights(url, dest, extract=True):
    start = time.time()
    print("downloading url: ", url)
    print("downloading to: ", dest)
    args = ["pget"]
    if extract:
        args.append("-x")
    subprocess.check_call(args + [url, dest], close_fds=False)
    print("downloading took: ", time.time() - start)


if __name__ == "__main__":
    print("Downloading models")
    download_weights(PHOTOMAKER_URL, PHOTOMAKER_PATH, extract=False)
    download_weights(BASE_MODEL_URL, BASE_MODEL_PATH)
    download_weights(SAFETY_URL, SAFETY_CACHE)