import pathlib
import requests
import yaml
from retrying import retry  # type: ignore
from tqdm import tqdm


@retry(
    stop_max_attempt_number=5, wait_fixed=2000
)  # Retry 5 times with a 2-second wait between every attempt
def download_file(url, local_filename, chunk_size):
    with requests.get(url, stream=True) as r:
        # raise exception if response is unsuccessfull
        r.raise_for_status()
        total_size = int(
            r.headers.get("content-length", 0)
        )  # Get the total size of the file
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
    home_dir = curr_dir.parent.parent.parent.as_posix()
    params = yaml.safe_load(open(f"{home_dir}/params.yaml"))[
        "fetch_data"
    ]  # load params.yaml file to access parameters

    file_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{params['year']}-{params['month']}.parquet"

    local_filename = file_url.split("/")[-1]
    local_filepath = pathlib.Path(
        f"{home_dir}/data/external/{local_filename}"
    )  # save data in ./data/external/ directory

    try:
        download_file(file_url, local_filepath, chunk_size=params["chunk_size"])
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the file after several attempts.\n{e}")
