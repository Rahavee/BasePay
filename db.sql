CREATE TABLE salary (
    "user_id" int,
    "job_id" int,
    "salary" int,
    "year" int
);

CREATE TABLE job_title (
    "job_id" SERIAL,
    "position" varchar(32)
);


CREATE TABLE names (
  "user_id" SERIAL,
  "first name" varchar(16),
  "last name" varchar(16)
);