from faker import Faker
import random

fake = Faker()

def get_registered_user():
    # Generate job history: between 1 and 3 jobs with experience from 1-10 years
    num_jobs = random.randint(1, 3)
    job_history = {}
    for _ in range(num_jobs):
        company = fake.company()
        years = random.randint(1, 10)
        job_history[company] = years
    return {
        "name": fake.name(),
        "address": fake.address(),
        "year_of_birth": fake.year(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "company": fake.company(),
        "job": fake.job(),
        "city": fake.city(),
        "country": fake.country(),
        "postcode": fake.postcode(),
        "job_history": job_history
    }