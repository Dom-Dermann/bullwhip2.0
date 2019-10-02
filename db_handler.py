import sqlite3
from sqlite3 import Error

### creation statements

create_companies_table = """CREATE TABLE IF NOT EXISTS companies (
    symbol text PRIMARY KEY,
    name text NOT NULL,
    invest integer,
    UNIQUE (symbol)
); """

create_yahoo_ratios_table = """ CREATE TABLE IF NOT EXISTS yahoo_ratios (
    ratio_id integer PRIMARY KEY,
    symbol text,
    year date,
    market_cap integer, 
    enterprise_value integer,
    trailing_pe integer,
    forward_pe integer,
    peg_ratio integer,
    price_sales integer,
    price_book integer,
    enterprise_value_revenue integer,
    enterprise_value_EBITDA integer,
    beta integer,
    year_change integer,
    SandP500_52_week_change integer,
    year_high integer, 
    year_low integer,
    fifty_day_moving_avg integer,
    twohundred_day_moving_avg integer,
    three_month_vol_avg integer,
    ten_day_vol_avg integer,
    shares_outstanding integer,
    float integer,
    percent_held_by_insiders integer,
    percent_held_by_institutions integer,
    shares_short integer, 
    short_ratio integer,
    short_percent_of_float integer,
    short_percent_of_shares_outstanding integer,
    share_short_perivous_month integer,
    forward_anual_dividend_rate integer,
    forward_anual_dividend_yield integer,
    trailing_anual_dividend_rate integer,
    trailing_anual_dividend_yield integer,
    five_year_average_dividend_yield integer,
    payout_ratio integer,
    dividend_date date,
    ex_dividend_date date,
    last_split_factor integer,
    last_split_date integer,
    fiscal_year_end date,
    most_recent_quarter date,
    profit_margin integer,
    operating_margin integer,
    return_on_assets integer,
    return_on_equity integer,
    revenue integer,
    revenue_per_share integer,
    quarterly_revenu_growth integer,
    gross_proft integer,
    EBITDA integer,
    net_income_avi_to_common integer,
    diluted_eps integer,
    quarterly_earnings_growth integer,
    total_cash integer,
    total_cash_per_share integer,
    total_debt integer,
    total_debt_equity integer,
    current_ratio integer,
    book_value_per_share integer,
    operating_cash_flow integer,
    levered_free_cash_flow integer,
    FOREIGN KEY (symbol) REFERENCES companies (symbol),
    UNIQUE(symbol, year)
); """

insert_yahoo_ratios_data = """
    INSERT OR IGNORE INTO yahoo_ratios(
    symbol,
    year,
    market_cap, 
    enterprise_value,
    trailing_pe,
    forward_pe,
    peg_ratio,
    price_sales,
    price_book,
    enterprise_value_revenue,
    enterprise_value_EBITDA,
    beta,
    year_change,
    SandP500_52_week_change,
    year_high, 
    year_low,
    fifty_day_moving_avg,
    twohundred_day_moving_avg,
    three_month_vol_avg,
    ten_day_vol_avg,
    shares_outstanding,
    float,
    percent_held_by_insiders,
    percent_held_by_institutions,
    shares_short, 
    short_ratio,
    short_percent_of_float,
    short_percent_of_shares_outstanding,
    share_short_perivous_month,
    forward_anual_dividend_rate,
    forward_anual_dividend_yield,
    trailing_anual_dividend_rate,
    trailing_anual_dividend_yield,
    five_year_average_dividend_yield,
    payout_ratio,
    dividend_date,
    ex_dividend_date,
    last_split_factor,
    last_split_date,
    fiscal_year_end,
    most_recent_quarter,
    profit_margin,
    operating_margin,
    return_on_assets,
    return_on_equity,
    revenue,
    revenue_per_share,
    quarterly_revenu_growth,
    gross_proft,
    EBITDA,
    net_income_avi_to_common,
    diluted_eps,
    quarterly_earnings_growth,
    total_cash,
    total_cash_per_share,
    total_debt,
    total_debt_equity,
    current_ratio,
    book_value_per_share,
    operating_cash_flow,
    levered_free_cash_flow
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
"""
### the API has potential to show all these:
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

insert_income_statement_data_sql = """ INSERT INTO income_statements (
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