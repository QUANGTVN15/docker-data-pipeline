# Created by Tran Vu Ngoc Quang - S3926943 - Big Data For Engineering
# Demo in this Google Drive link: https://drive.google.com/file/d/10BEQ0CURrU7Z5p69FYqSv-yVoT3xJPT6/view?usp=sharing

# Data pipeline using Docker (Cassandra, Kafka, Python, Notebook)
This project will build a simple datapipeline with detailed instruction

# Prerequisite
Please register for OpenweathermapAPI and SuperheroAPI to get an API key for them. Here is the link
https://openweathermap.org/

# Additional API
About JokeAPI
Name: JokeAPI

Official Website: https://jokeapi.dev/

Docs: https://jokeapi.dev/

Status: Public, free, no API key required for basic use


# Instructions

## Create docker networks
```bash
docker network create kafka-network
docker network create cassandra-network
```

## Starting Cassandra
Setup Cassandra first. Double check that it completely established before moving on to the next step.
```bash
docker-compose -f cassandra/docker-compose.yml up -d --build
docker exec -it cassandra bash
cqlsh -f schema-faker.cql #Make table if not exist for FAKER
cqlsh -f schema-joke.cql #Make table if not exist for JOKE

# Check Table or Old Data
cqlsh --cqlversion=3.4.4 127.0.0.1 
use kafkapipeline;
select * from weatherreport;
select * from fakerdata;
select * from jokedata;
```

## Starting Kafka on Docker and create sink
```bash
docker-compose -f kafka/docker-compose.yml up -d --build
#Go to http://localhost:9000 and create a Cluster before running the code below in kafka-connect CLI
./start-and-wait.sh
```

## Starting Openweathermap Producer
```bash
docker-compose -f owm-producer/docker-compose.yml up -d
```

## Starting FakerAPI Producer
```bash
docker-compose -f faker-producer/docker-compose.yml up -d
```

## Starting JokeAPI Producer
```bash
docker-compose -f joke-producer/docker-compose.yml up -d --build
```

## Starting Consumer
``` bash
docker-compose -f consumers/docker-compose.yml up --build
```

## Visualization

Run the following command then go to http://localhost:8888 and run the visualization notebook accordingly

``` bash
docker-compose -f data-vis/docker-compose.yml up -d --build
```

## Teardown

Remove all running container

```bash
docker rm -f $(docker ps -a -q)
```

Remove the networks

```bash
docker network rm kafka-network
docker network rm cassandra-network
```

To remove resources in Docker

```bash
docker container prune # remove stopped containers, done with the docker-compose down
docker volume prune # remove all dangling volumes (delete all data from your Kafka and Cassandra)
docker image prune -a # remove all images (help with rebuild images)
docker builder prune # remove all build cache (you have to pull data again in the next build)
docker system prune -a # basically remove everything
```

## Data Analysis:
1. Weather report plot: 
- Especially important to be able to filter the data by city, allowing the capability to administrate the weather state of the world among the huge data being created throughout the world. We can leverage this for professional to take actions whenever insights are gathered quickly.
- The relationship between numerical data in a time-series situation shows how different aspects affect eachother in real time. The ability to observe the relationship with just a heatmap is a big step in the research field, allowing data to be fully observed from a bigger perspective.

2. Faker data plot:
- The data gathered with details, especially in the terms that a person working at a company for how long is recorded, may helps employer find their next potential employee easier. Understanding the insight of number and text, we can effectively find what we need in seconds. Among 2000 people, 571 people who worked at one company for more than 9 years were found. 

3. Joke data plot:
- The joke being tokenized in to levels allow Large Language Model (LLM) developer to easily filter out datapoints that take up too much computational resource just for training. Training AI is not just a matter of time and technique, it is a problem of resource as models are more than ever smarter and taking more energy. The management of data being fed to an AI must be controlled for the future of a sustainable world. 

