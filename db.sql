CREATE TABLE salary (
    "user_id" int,
    "job_id" int,
    "pay" varchar(16),
    "year" int
);

CREATE TABLE job_title (
    "job_id" SERIAL,
    "position" varchar(32)
);


CREATE TABLE names (
  "user_id" SERIAL,
  "first_name" varchar(32),
  "last_name" varchar(32)
);