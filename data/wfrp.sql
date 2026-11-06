CREATE TYPE "skill_kind" AS ENUM (
  'base',
  'advanced'
);

CREATE TYPE "status_tier_enum" AS ENUM (
  'Brass',
  'Silver',
  'Gold'
);

CREATE TYPE "characteristic_enum" AS ENUM (
  'WS',
  'BS',
  'S',
  'T',
  'I',
  'Ag',
  'Dex',
  'Int',
  'WP',
  'Fel'
);

CREATE TABLE "species" (
  "id" integer PRIMARY KEY,
  "name" varchar NOT NULL,
  "base_move" integer NOT NULL,
  "base_fate" integer NOT NULL,
  "base_resilience" integer NOT NULL,
  "extra_points" integer NOT NULL,
  "wounds_formula" varchar NOT NULL
);

CREATE TABLE "species_characteristic_base" (
  "species_id" integer NOT NULL,
  "characteristic" characteristic_enum NOT NULL,
  "base_value" integer NOT NULL,
  PRIMARY KEY ("species_id", "characteristic")
);

CREATE TABLE "classes" (
  "id" integer PRIMARY KEY,
  "name" varchar NOT NULL,
  "starting_trappings" text NOT NULL
);

CREATE TABLE "careers" (
  "id" integer PRIMARY KEY,
  "class_id" integer NOT NULL NOT NULL,
  "name" varchar NOT NULL
);

CREATE TABLE "career_species_roll" (
  "career_id" integer NOT NULL,
  "species_id" integer NOT NULL,
  "roll_min" integer NOT NULL,
  "roll_max" integer NOT NULL,
  PRIMARY KEY ("career_id", "species_id")
);

CREATE TABLE "career_levels" (
  "id" integer PRIMARY KEY,
  "career_id" integer NOT NULL,
  "level" integer NOT NULL,
  "title" varchar NOT NULL,
  "status_tier" status_tier_enum NOT NULL,
  "standing" integer NOT NULL,
  "trappings" text NOT NULL
);

CREATE TABLE "skills" (
  "id" integer PRIMARY KEY,
  "name" varchar NOT NULL,
  "kind" skill_kind NOT NULL,
  "characteristic" characteristic_enum NOT NULL,
  "grouped" boolean 
);

CREATE TABLE "talents" (
  "id" integer PRIMARY KEY,
  "name" varchar NOT NULL,
  "max_times" varchar NOT NULL,
  "description" text NOT NULL
);

CREATE TABLE "career_level_skills" (
  "career_level_id" integer NOT NULL,
  "skill_id" integer NOT NULL,
  PRIMARY KEY ("career_level_id", "skill_id")
);

CREATE TABLE "career_level_talents" (
  "career_level_id" integer NOT NULL,
  "talent_id" integer NOT NULL,
  PRIMARY KEY ("career_level_id", "talent_id")
);

CREATE TABLE "career_level_characteristics" (
  "career_level_id" integer NOT NULL,
  "characteristic" characteristic_enum NOT NULL,
  PRIMARY KEY ("career_level_id", "characteristic")
);

CREATE TABLE "species_skills" (
  "id" integer PRIMARY KEY,
  "species_id" integer NOT NULL,
  "skill_id" integer NOT NULL,
  "choice_group" integer NOT NULL
);

CREATE TABLE "species_talents" (
  "id" integer PRIMARY KEY,
  "species_id" integer NOT NULL,
  "talent_id" integer NOT NULL,
  "choice_group" integer NOT NULL
);

CREATE TABLE "characters" (
  "id" integer PRIMARY KEY,
  "name" varchar NOT NULL,
  "species_id" integer NOT NULL,
  "current_career_level_id" integer NOT NULL,
  "wounds" integer NOT NULL,
  "fate" integer NOT NULL,
  "fortune" integer NOT NULL,
  "resilience" integer NOT NULL,
  "resolve" integer NOT NULL
);

CREATE TABLE "character_characteristics" (
  "character_id" integer NOT NULL,
  "characteristic" characteristic_enum NOT NULL,
  "initial_value" integer NOT NULL,
  "advances" integer NOT NULL,
  PRIMARY KEY ("character_id", "characteristic")
);

CREATE TABLE "character_skills" (
  "character_id" integer NOT NULL ,
  "skill_id" integer NOT NULL ,
  "advances" integer NOT NULL ,
  PRIMARY KEY ("character_id", "skill_id")
);

CREATE TABLE "character_talents" (
  "character_id" integer NOT NULL,
  "talent_id" integer NOT NULL,
  "times_taken" integer NOT NULL,
  PRIMARY KEY ("character_id", "talent_id")
);

CREATE TABLE "character_trappings" (
  "id" integer PRIMARY KEY,
  "character_id" integer NOT NULL,
  "name" varchar NOT NULL,
  "quantity" integer NOT NULL,
  "description" text NOT NULL
);

COMMENT ON COLUMN "species_skills"."choice_group" IS 'Pour regrouper les options "X ou Y"';

COMMENT ON COLUMN "species_talents"."choice_group" IS 'Pour regrouper les options "X ou Y"';

ALTER TABLE "species_characteristic_base" ADD FOREIGN KEY ("species_id") REFERENCES "species" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "careers" ADD FOREIGN KEY ("class_id") REFERENCES "classes" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "career_species_roll" ADD FOREIGN KEY ("career_id") REFERENCES "careers" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "career_species_roll" ADD FOREIGN KEY ("species_id") REFERENCES "species" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "career_levels" ADD FOREIGN KEY ("career_id") REFERENCES "careers" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "career_level_skills" ADD FOREIGN KEY ("career_level_id") REFERENCES "career_levels" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "career_level_skills" ADD FOREIGN KEY ("skill_id") REFERENCES "skills" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "career_level_talents" ADD FOREIGN KEY ("career_level_id") REFERENCES "career_levels" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "career_level_talents" ADD FOREIGN KEY ("talent_id") REFERENCES "talents" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "career_level_characteristics" ADD FOREIGN KEY ("career_level_id") REFERENCES "career_levels" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "species_skills" ADD FOREIGN KEY ("species_id") REFERENCES "species" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "species_skills" ADD FOREIGN KEY ("skill_id") REFERENCES "skills" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "species_talents" ADD FOREIGN KEY ("species_id") REFERENCES "species" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "species_talents" ADD FOREIGN KEY ("talent_id") REFERENCES "talents" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "characters" ADD FOREIGN KEY ("species_id") REFERENCES "species" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "characters" ADD FOREIGN KEY ("current_career_level_id") REFERENCES "career_levels" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "character_characteristics" ADD FOREIGN KEY ("character_id") REFERENCES "characters" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "character_skills" ADD FOREIGN KEY ("character_id") REFERENCES "characters" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "character_skills" ADD FOREIGN KEY ("skill_id") REFERENCES "skills" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "character_talents" ADD FOREIGN KEY ("character_id") REFERENCES "characters" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "character_talents" ADD FOREIGN KEY ("talent_id") REFERENCES "talents" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "character_trappings" ADD FOREIGN KEY ("character_id") REFERENCES "characters" ("id") DEFERRABLE INITIALLY IMMEDIATE;
