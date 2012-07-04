--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: voters; Type: TABLE; Schema: public; Owner: eric; Tablespace: 
--

CREATE TABLE voters (
    voterid integer,
    county character varying(50),
    first_name character varying(33),
    middle_name character varying(31),
    last_name character varying(33),
    suffix character varying(10),
    birthdate character varying(25),
    registrationdate character varying(25),
    address1 character varying(100),
    address2 character varying(100),
    city character varying(50),
    state character varying(2),
    zip character varying(12),
    phone character varying(24),
    party character varying(50),
    congressionaldistrict character varying(1),
    senatedistrict character varying(50),
    assemblydistrict character varying(25),
    educationdistrict character varying(25),
    regentdistrict character varying(25),
    registeredprecinct character varying(10),
    countystatus character varying(10),
    countyvoterid character varying(12),
    idrequired character varying(1)
);


ALTER TABLE public.voters OWNER TO eric;

ALTER TABLE ONLY voters
    ADD CONSTRAINT voters_voterid_key UNIQUE (voterid);

CREATE INDEX voters_voterid ON voters USING btree (voterid);
CREATE INDEX voters_county ON voters USING btree (county);
