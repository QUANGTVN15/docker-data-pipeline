USE kafkapipeline;

CREATE TABLE IF NOT EXISTS kafkapipeline.fakerdata (
  name TEXT,
  address TEXT,
  year_of_birth INT,
  email TEXT,
  phone_number TEXT,
  company TEXT,
  job TEXT,
  city TEXT,
  country TEXT,
  postcode TEXT,
  job_history MAP<TEXT, INT>,
  PRIMARY KEY (name, address)
);