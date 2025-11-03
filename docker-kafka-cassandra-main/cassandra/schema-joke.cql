USE kafkapipeline;
CREATE TABLE IF NOT EXISTS jokedata (
    id int,
    category text,
    type text,
    joke text,
    setup text,
    delivery text,
    lang text,
    flags map<text, boolean>,
    PRIMARY KEY (id)
);