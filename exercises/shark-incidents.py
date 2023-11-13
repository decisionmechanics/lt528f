import polars as pl

df = pl.scan_csv(
    "shark-incidents.csv", infer_schema_length=None, truncate_ragged_lines=True
).collect()

dangerous_sharks_df = (
    df.filter(
        (pl.col("Victim.injury") == "fatal")
        & (pl.col("Shark.common.name").is_not_null())
    )
    .group_by("Shark.common.name")
    .agg(pl.count())
    .select(species="Shark.common.name", count="count")
    .sort("count", descending=True)
)

for dangerous_shark in dangerous_sharks_df.rows(named=True):
    print(
        f"{dangerous_shark['species']}s were responsible for {dangerous_shark['count']} attack(s)"
    )
