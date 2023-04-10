from fastapi import FastAPI
from database import create_tables
from pydantic import BaseModel
from geopy import distance
import uvicorn
import sqlite3
import os

app = FastAPI()

create_tables()

db_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "addresses.db")


class Address(BaseModel):
    id: int = None
    name: str
    address: str
    latitude: float
    longitude: float

    def distance_to(self, other):
        return distance.distance((self.latitude, self.longitude), (other.latitude, other.longitude)).km


class AddressDB:
    def __init__(self):
        self.conn = sqlite3.connect(f"file:{db_file}?mode=rw", uri=True, check_same_thread=False)

    def get_all_addresses(self):
        c = self.conn.cursor()
        c.execute("SELECT id, name, address, latitude, longitude FROM addresses")
        rows = c.fetchall()
        addresses = []
        for row in rows:
            address = Address(id=row[0], name=row[1], address=row[2], latitude=row[3], longitude=row[4])
            addresses.append(address)
        return addresses

    def add_address(self, address):
        c = self.conn.cursor()
        c.execute("INSERT INTO addresses (name, address, latitude, longitude) VALUES (?, ?, ?, ?)",
                  (address.name, address.address, address.latitude, address.longitude))
        self.conn.commit()
        address.id = c.lastrowid
        return address

    def update_address(self, address):
        c = self.conn.cursor()
        c.execute("UPDATE addresses SET name=?, address=?, latitude=?, longitude=? WHERE id=?",
                  (address.name, address.address, address.latitude, address.longitude, address.id))
        self.conn.commit()

    def delete_address(self, id):
        c = self.conn.cursor()
        c.execute("DELETE FROM addresses WHERE id=?", (id,))
        self.conn.commit()

    def get_address(self, id):
        c = self.conn.cursor()
        c.execute("SELECT id, name, address, latitude, longitude FROM addresses WHERE id=?", (id,))
        row = c.fetchone()
        if row is None:
            return None
        return Address(id=row[0], name=row[1], address=row[2], latitude=row[3], longitude=row[4])

    def get_addresses_within_distance(self, latitude, longitude, max_distance):
        c = self.conn.cursor()
        c.execute("SELECT id, name, address, latitude, longitude FROM addresses WHERE "
                  "((latitude - ?) * (latitude - ?) + (longitude - ?) * (longitude - ?)) <= ? * ?",
                  (latitude, latitude, longitude, longitude, max_distance, max_distance))
        rows = c.fetchall()
        addresses = []
        for row in rows:
            address = Address(id=row[0], name=row[1], address=row[2], latitude=row[3], longitude=row[4])
            addresses.append(address)
        return addresses


db = AddressDB()


@app.get("/all_addresses")
def read_all_addresses():
    return db.get_all_addresses()


@app.post("/addresses")
def create_address(address: Address):
    return db.add_address(address)


@app.put("/addresses/{id}")
def update_address(id: int, address: Address):
    address.id = id
    db.update_address(address)


@app.delete("/addresses/{id}")
def delete_address(id: int):
    db.delete_address(id)


@app.get("/addresses/{id}")
def read_address(id: int):
    return db.get_address(id)


@app.get("/addresses")
def read_addresses(latitude: float, longitude: float, max_distance: float):
    return db.get_addresses_within_distance(latitude, longitude, max_distance)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
