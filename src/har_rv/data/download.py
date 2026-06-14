from datetime import datetime
from pathlib import Path
import dukascopy_python
from dukascopy_python.instruments import INSTRUMENT_FX_CROSSES_USD_ZAR

OFFER_SIDES = {
    "bid": dukascopy_python.OFFER_SIDE_BID,
    "ask": dukascopy_python.OFFER_SIDE_ASK,
}

for side_name, offer_side in OFFER_SIDES.items():
    raw_dir = Path(f"data/raw/usdzar_1min_{side_name}")
    raw_dir.mkdir(parents=True, exist_ok=True)

    for year in range(2012, 2027):
        out_path = raw_dir / f"usdzar_1min_{side_name}_{year}.parquet"
        if out_path.exists():
            print(f"{side_name} {year}: already downloaded, skipping")
            continue

        start = datetime(year, 1, 1)
        end = min(datetime(year + 1, 1, 1), datetime.now())

        print(f"{side_name} {year}: fetching {start.date()} to {end.date()}...")
        df = dukascopy_python.fetch(
            instrument=INSTRUMENT_FX_CROSSES_USD_ZAR,
            interval=dukascopy_python.INTERVAL_MIN_1,
            offer_side=offer_side,
            start=start,
            end=end,
            max_retries=5,
        )
        df.to_parquet(out_path)
        print(f"{side_name} {year}: saved {df.shape[0]} rows")