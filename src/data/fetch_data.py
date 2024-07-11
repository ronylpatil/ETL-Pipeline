import pathlib
import requests
from retrying import retry # type: ignore
from tqdm import tqdm


@retry(
    stop_max_attempt_number=5, wait_fixed=2000
)  # Retry 5 times with a 2-second wait between every attempt
def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        # raise exception if response is unsuccessfull
        r.raise_for_status()
        total_size = int(
            r.headers.get("content-length", 0)
        )  # Get the total size of the file
        chunk_size = 8192
        with open(local_filename, "wb") as f:
            for chunk in tqdm(
                r.iter_content(chunk_size=chunk_size),
                total=total_size // chunk_size,
                unit="KB",
            ):
                f.write(chunk)

    print(f"File downloaded successfully!!!")


if __name__ == "__main__":

    curr_dir = pathlib.Path(__file__)
    home_dir = curr_dir.parent.parent.parent

    year = "2019"
    month = "011"
    file_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month}.parquet"

    local_filename = file_url.split("/")[-1]
    local_filepath = pathlib.Path(f"{home_dir.as_posix()}/{local_filename}")

    try:
        download_file(file_url, local_filename)
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the file after several attempts.\n{e}")
