CREATE INDEX voters_name_idx
ON voters
USING gin(to_tsvector('english', last_name || ' ' || first_name));

CREATE INDEX voters_address_idx
ON voters
USING gin(to_tsvector('english', address1));
