from signalrcore.hub_connection_builder import HubConnectionBuilder
import logging
import requests
import json
import time
import os
import datetime
import mysql.connector


class Main:
    def __init__(self):
        self._hub_connection = None
        self.HOST = os.environ.get("HOST", "http://34.95.34.5")
        self.TOKEN = os.environ.get("TOKEN", "Default")
        self.TICKETS = os.environ.get("TICKETS", 10)
        self.T_MAX = os.environ.get("T_MAX", 90)
        self.T_MIN = os.environ.get("T_MIN", 10)
        self.DB_HOST = os.environ.get("DB_HOST", "Default")
        self.DB_NAME = os.environ.get("DB_NAME", "Default")
        self.DB_USER = os.environ.get("DB_USER", "Default")
        self.DB_PASSWORD = os.environ.get("DB_PASSWORD", "Default")

    def __del__(self):
        if self._hub_connection != None:
            self._hub_connection.stop()

    def setup(self):
        self.setSensorHub()

    def start(self):
        self.setup()
        self._hub_connection.start()

        print("Press CTRL+C to exit.")
        while True:
            time.sleep(2)

    def setSensorHub(self):
        self._hub_connection = (
            HubConnectionBuilder()
            .with_url(f"{self.HOST}/SensorHub?token={self.TOKEN}")
            .configure_logging(logging.INFO)
            .with_automatic_reconnect(
                {
                    "type": "raw",
                    "keep_alive_interval": 10,
                    "reconnect_interval": 5,
                    "max_attempts": 999,
                }
            )
            .build()
        )

        self._hub_connection.on("ReceiveSensorData", self.onSensorDataReceived)
        self._hub_connection.on_open(lambda: print("||| Connection opened."))
        self._hub_connection.on_close(lambda: print("||| Connection closed."))
        self._hub_connection.on_error(
            lambda data: print(f"||| An exception was thrown closed: {data.error}")
        )

    def onSensorDataReceived(self, data):
        try:
            print(data[0]["date"] + " --> " + data[0]["data"])
            date = data[0]["date"]
            dp = float(data[0]["data"])
            self.send_temperature_to_database(dp)
            self.analyzeDatapoint(date, dp)
        except Exception as err:
            print(err)

    def analyzeDatapoint(self, date, data):
        if float(data) >= float(self.T_MAX):
            self.sendActionToHvac(date, "TurnOnAc", self.TICKETS)
        elif float(data) <= float(self.T_MIN):
            self.sendActionToHvac(date, "TurnOnHeater", self.TICKETS)

    def sendActionToHvac(self, date, action, nbTick):
        r = requests.get(f"{self.HOST}/api/hvac/{self.TOKEN}/{action}/{nbTick}")
        details = json.loads(r.text)
        self.send_event_to_database(action + " : " + str(nbTick))
        print(details)

    def send_event_to_database(self, event):
        try:
            mydb = mysql.connector.connect(
                host=self.DB_HOST,
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                database=self.DB_NAME,
            )

            mycursor = mydb.cursor()

            sql = "INSERT INTO hvac_events (action) VALUES (%s)"
            val = event
            mycursor.execute(sql, val)

            mydb.commit()
            mydb.close()

            print(mycursor.rowcount, "record inserted.")
            pass
        except Exception as e:
            print(e)
            pass

    def send_temperature_to_database(self, data):
        try:
            mydb = mysql.connector.connect(
                host=self.DB_HOST,
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                database=self.DB_NAME,
            )

            mycursor = mydb.cursor()

            sql = "INSERT INTO hvac_temps (temperature) VALUES (%s)"
            val = data
            mycursor.execute(sql, val)

            mydb.commit()
            mydb.close()

            print(mycursor.rowcount, "record inserted.")
            pass
        except Exception as e:
            print(e)
            pass


if __name__ == "__main__":
    main = Main()
    main.start()
