# **Optimizing-Public-Transportation**

## **Architecture**

### **Overview**
This project is a part of the Udacity Data Streaming Nanodegree. It constructs a real-time streaming event pipeline using Apache Kafka and its ecosystem. Leveraging public datasets from the Chicago Transit Authority, we simulate and display train status updates in real time.

### **Pipeline Components**
- **Arrivals and Turnstiles** → Producers that generate train arrival and turnstile entry events into the Kafka cluster.
  - **Arrivals** indicate when a train has arrived at a station.
  - **Turnstiles** log passenger entries into the station.
- **Weather** → A REST Proxy producer that periodically fetches weather data and emits it to the Kafka cluster.
- **PostgreSQL & Kafka Connect** → Extracts station data from PostgreSQL and publishes it to Kafka.
- **Kafka Status Server** → Consumes data from Kafka topics and displays it on the UI.

## **Results**
This architecture enables real-time monitoring and analytics of Chicago's public transit system, improving efficiency and passenger experience.

---

## **Environment Setup**
### **Dependencies**
- **Docker** (using the Bitnami Kafka image)
- **Python 3.7**

### **Running and Testing**
#### **Start Services**
Ensure all services are up and running using Docker:
```sh
docker-compose up
```
> **Note:** Docker Compose may take 3-5 minutes to fully start, depending on your hardware. Verify services using the provided Docker URLs.

#### **Install Dependencies**
For producers:
```sh
cd producers
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```
For consumers:
```sh
cd consumers
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

---

## **Running the Simulation**

### **Start Producers**
Simulate train arrivals and turnstile events:
```sh
cd producers
python simulation.py
```

### **Run Faust Stream Processing**
```sh
cd consumers
faust -A faust_stream worker -l info
```

### **Run KSQL Consumer**
```sh
cd consumers
python ksql.py
```

### **Start Kafka Consumer Server**
```sh
cd consumers
python server.py
```

---

## **Resources**
- [Confluent Python Client Documentation](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html)
- [Confluent Python Client Usage and Examples](https://github.com/confluentinc/confluent-kafka-python)
- [REST Proxy API Reference](https://docs.confluent.io/platform/current/kafka-rest/api.html)
- [Kafka Connect JDBC Source Connector Configuration Options](https://docs.confluent.io/platform/current/connect/kafka-connect-jdbc/source-connector/index.html)

# Optimizing-Public-Transportation
