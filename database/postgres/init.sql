--------------------------------------------------------------------------------
-- Table: stock_symbol
--------------------------------------------------------------------------------

DROP TABLE IF EXISTS stock_symbol;

CREATE TABLE stock_symbol
(
  creation_dt timestamp without time zone DEFAULT now(),
  release_date date NOT NULL,
  stock_symbol text NOT NULL,
  stock_name text,
  isin_code text,
  listing_date date,
  market_category text,
  industry_category text,
  cfi_code text,
  CONSTRAINT stock_symbol_unique_key UNIQUE (release_date, stock_symbol)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE stock_symbol
  OWNER TO stockcat;

--------------------------------------------------------------------------------
-- Table: capital_increase_history
--------------------------------------------------------------------------------

DROP TABLE IF EXISTS capital_increase_history;

CREATE TABLE capital_increase_history
(
  creation_dt timestamp without time zone DEFAULT now(),
  release_date date NOT NULL,
  stock_symbol text NOT NULL,
  stmt_date date NOT NULL,
  account text NOT NULL,
  account_order smallint NOT NULL,
  value double precision,
  CONSTRAINT capital_increase_history_unique_key UNIQUE (release_date, stock_symbol, stmt_date, account, account_order)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE capital_increase_history
  OWNER TO stockcat;

--------------------------------------------------------------------------------
-- Table: dividend_policy
--------------------------------------------------------------------------------

DROP TABLE IF EXISTS dividend_policy;

CREATE TABLE dividend_policy
(
  creation_dt timestamp without time zone DEFAULT now(),
  release_date date NOT NULL,
  stock_symbol text NOT NULL,
  stmt_date date NOT NULL,
  account text NOT NULL,
  account_order smallint NOT NULL,
  value double precision,
  CONSTRAINT dividend_policy_unique_key UNIQUE (release_date, stock_symbol, stmt_date, account, account_order)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE dividend_policy
  OWNER TO stockcat;  

--------------------------------------------------------------------------------
-- Table: profitability
--------------------------------------------------------------------------------

DROP TABLE IF EXISTS profitability;

CREATE TABLE profitability
(
  creation_dt timestamp without time zone DEFAULT now(),
  release_date date NOT NULL,
  stock_symbol text NOT NULL,
  stmt_date date NOT NULL,
  account text NOT NULL,
  account_order smallint NOT NULL,
  value double precision,
  CONSTRAINT profitability_unique_key UNIQUE (release_date, stock_symbol, stmt_date, account, account_order)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE profitability
  OWNER TO stockcat;
