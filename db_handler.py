import sqlite3
from sqlite3 import Error

### creation statements

create_companies_table = """CREATE TABLE IF NOT EXISTS companies (
    symbol text PRIMARY KEY,
    name text NOT NULL,
    invest integer,
    UNIQUE (symbol)
); """

### the API has potential to show all these for income statements:
    # year date, 
    # revenue integer, 
    # revenue_growrth integer, 
    # cost_of_revenue integer,
    # gross_profit integer,
    # rnd_expenses integer,
    # sga_expenses integer,
    # operating_expenses integer,
    # operating_income integer,
    # interest_expense integer,
    # EBT integer,
    # income_tax_expense integer,
    # net_income_non_controlling integer,
    # net_income_destributed_ops integer,
    # net_income integer,
    # preferred_dividends integer,
    # net_income_com integer,
    # EPS integer,
    # EPS_diluted integer,
    # weighted_average_shs_out integer,
    # weighted_average_shs_out_dil integer,
    # dividend_per_share intger,
    # gross_margin integer,
    # EBITDA_margin integer,
    # EBIT_margin integer,
    # profit_margin integer,
    # free_cash_flow_margin integer,
    # EBITDA integer,
    # EBIT integer,
    # consolidated_income integer,
    # EBT_margin integer,
    # net_profit_margin intger,
create_income_statements_table = """ CREATE TABLE IF NOT EXISTS income_statements (
    id integer PRIMARY KEY, 
    symbol text,
    date date, 
    revenue integer, 
    revenue_growth integer, 
    cost_of_revenue integer,
    gross_profit integer,
    rnd_expenses integer,
    sga_expenses integer,
    operating_expenses integer,
    operating_income integer,
    interest_expense integer,
    EBT integer,
    income_tax_expense integer,
    net_income integer,
    EPS integer,
    dividend_per_share intger,
    gross_margin integer,
    EBITDA_margin integer,
    EBIT_margin integer,
    profit_margin integer,
    free_cash_flow_margin integer,
    EBITDA integer,
    EBIT integer,
    EBT_margin integer,
    net_profit_margin integer,
    FOREIGN KEY (symbol) REFERENCES companies (symbol),
    UNIQUE(symbol, date)
);"""

insert_income_statement_data_sql = """ INSERT OR IGNORE INTO income_statements (
    symbol,
    date, 
    revenue, 
    revenue_growth, 
    cost_of_revenue,
    gross_profit,
    rnd_expenses,
    sga_expenses,
    operating_expenses,
    operating_income,
    interest_expense,
    EBT,
    income_tax_expense,
    net_income,
    EPS,
    dividend_per_share,
    gross_margin,
    EBITDA_margin,
    EBIT_margin,
    profit_margin,
    free_cash_flow_margin,
    EBITDA,
    EBIT,
    EBT_margin,
    net_profit_margin
    ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """


### the API has potential to show all these for income statements:
#     date date,
#     cash_and_equivalents integer, 
#     short_term_investments integer,
#     cash_and_short_term_investements integer,
#     receiveables integer, 
#     inventories integer,
#     total_current_assets integer,
#     property_plant_equipment integer,
#     goodwill_intangible integer, 
#     long_term_investments integer,
#     tax_assets integer,
#     total_non_current_assets integer,
#     total_assets integer,
#     payables integer,
#     short_term_debt integer, 
#     total_current_liabilities integer,
#     long_term_debt integer,
#     total_debt integer,
#     deffered_revenue integer,
#     tax_liabilities integer,
#     deposit_liabilities integer,
#     total_non_current_liabilities integer,
#     total_liabilities integer, 
#     other_comprehensive_income integer,
#     retained_earnings integer,
#     total_shareholders_equity integer,
#     investments integer,
#     net_debt integer,
#     other_assets integer, 
#     other_liabilities integer,

create_balance_sheets_table_sql = """ CREATE TABLE IF NOT EXISTS balance_sheets (
    id integer PRIMARY KEY,
    symbol text, 
    date date,
    cash_and_equivalents integer, 
    short_term_investments integer,
    receiveables integer, 
    inventories integer,
    total_current_assets integer,
    property_plant_equipment integer,
    goodwill_intangible integer, 
    long_term_investments integer,
    total_non_current_assets integer,
    total_assets integer,
    payables integer,
    short_term_debt integer, 
    total_current_liabilities integer,
    long_term_debt integer,
    total_debt integer,
    deffered_revenue integer,
    tax_liabilities integer,
    deposit_liabilities integer,
    total_non_current_liabilities integer,
    total_liabilities integer, 
    retained_earnings integer,
    total_shareholders_equity integer,
    investments integer,
    net_debt integer,
    other_assets integer, 
    other_liabilities integer,
    FOREIGN KEY (symbol) REFERENCES companies (symbol),
    UNIQUE(symbol, date)
);
"""

### DB methods

def create_connection(db_file):
    # create connection to sqlite db
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('connected to DB version: ' + sqlite3.version)
        return conn
    except Error as e: 
        print(e)
    
    return conn

def close_connection(conn):
    conn.close()
    return True

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_company_data(conn, symbol, name, invest):
    sql = "INSERT OR IGNORE INTO companies VALUES (?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, [symbol, name, invest])
    conn.commit

def insert_income_statement_data(conn, income_statement):
    cur = conn.cursor()
    cur.execute(insert_income_statement_data_sql, income_statement)
    conn.commit()
    return cur.lastrowid

def insert_key_ratio_data(con, key_ratios):
    cur = con.cursor()
    cur.execute(insert_yahoo_ratios_data, key_ratios)
    con.commit()
    return cur.lastrowid

### for testing only
def main():
    database = "./stock_db.db"
    
    # create connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, create_companies_table)
        create_table(conn, create_income_statements_table)
        conn.commit()
    else:
        print('Error, DB connection not established.')

if __name__ == "__main__":
    main()