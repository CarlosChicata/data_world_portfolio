-- Table: operational.branch_schedule

-- DROP TABLE IF EXISTS operational.branch_schedule;

CREATE TABLE IF NOT EXISTS operational.branch_schedule
(	
	open_time time without time zone,
	close_time time without time zone,
	branch_id integer NOT NULL,
	days operational.days
    id_internal serial NOT NULL,
    start_lifecycle timestamp without time zone NOT NULL DEFAULT now(),
    end_lifecycle timestamp without time zone,
    creation timestamp without time zone NOT NULL DEFAULT now(),
    is_delete boolean NOT NULL DEFAULT false,
    CONSTRAINT branch_id_idx PRIMARY KEY (id_internal),
    CONSTRAINT branch_city_id FOREIGN KEY (branch_id)
        REFERENCES operational.branch (id_register) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS operational.branch_schedule
    OWNER to postgres;