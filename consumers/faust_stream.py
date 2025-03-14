"""Defines trends calculations for stations"""
import logging

import faust


logger = logging.getLogger(__name__)


# Faust will ingest records from Kafka in this format
class Station(faust.Record):
    stop_id: int
    direction_id: str
    stop_name: str
    station_name: str
    station_descriptive_name: str
    station_id: int
    order: int
    red: bool
    blue: bool
    green: bool


# Faust will produce records to Kafka in this format
class TransformedStation(faust.Record):
    station_id: int
    station_name: str
    order: int
    line: str


app = faust.App("stations-stream", broker="kafka://localhost:9092", store="memory://")

topic = app.topic("connect-stations", value_type=Station)

out_topic = app.topic("faust.stations.transformed", partitions=1)

table = app.Table(
   "faust.stations.transformed.table",
   default=TransformedStation,
   partitions=1,
   changelog_topic=out_topic,
)


#
#
# TODO: Using Faust, transform input `Station` records into `TransformedStation` records. Note that
# "line" is the color of the station. So if the `Station` record has the field `red` set to true,
# then you would set the `line` of the `TransformedStation` record to the string `"red"`
#
#
@app.agent(topic)
async def transform_station_line(stations): 
    async for station in stations:  
        if station.red:
            line = "red"
        elif station.blue:
            line = "blue"
        elif station.green:
            line = "green"
        else:
            line = "unknown"
            
        # Create transformed station
        transformed_station = TransformedStation(
            station_id=station.station_id,
            station_name=station.station_name,
            order=station.order,
            line=line,
        )
        
        # Store in table
        table[station.station_id] = transformed_station
        # Publish to topic
        await out_topic.send(value=transformed_station)


if __name__ == "__main__":
    app.main()
