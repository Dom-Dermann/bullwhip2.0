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
    # net_profit_margin intger

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

insert_balance_sheet_data_sql = """ INSERT OR IGNORE INTO balance_sheets (
    symbol, 
    date,
    cash_and_equivalents, 
    short_term_investments,
    receiveables, 
    inventories,
    total_current_assets,
    property_plant_equipment,
    goodwill_intangible, 
    long_term_investments,
    total_non_current_assets,
    total_assets,
    payables,
    short_term_debt, 
    total_current_liabilities,
    long_term_debt,
    total_debt,
    deffered_revenue,
    tax_liabilities,
    deposit_liabilities,
    total_non_current_liabilities,
    total_liabilities, 
    retained_earnings,
    total_shareholders_equity,
    investments,
    net_debt,
    other_assets, 
    other_liabilities
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

### API has potential show show all these for cash flow statements:
# date: "2018-09-29",
# Depreciation & Amortization: "10903000000.0",
# Stock-based compensation: "5340000000.0",
# Operating Cash Flow: "77434000000.0",
# Capital Expenditure: "-13313000000.0",
# Acquisitions and disposals: "-721000000.0",
# Investment purchases and sales: "30845000000.0",
# Investing Cash flow: "16066000000.0",
# Issuance (repayment) of debt: "432000000.0",
# Issuance (buybacks) of shares: "-72069000000.0",
# Dividend payments: "-13712000000.0",
# Financing Cash Flow: "-87876000000.0",
# Effect of forex changes on cash: "0.0",
# Net cash flow / Change in cash: "5624000000.0",
# Free Cash Flow: "64121000000.0",
# Net Cash/Marketcap: "-0.0439"

create_cash_flow_table_sql = """ CREATE TABLE IF NOT EXISTS cash_flows (
    id integer PRIMARY KEY,
    symbol text, 
    date date, 
    Depreciation_Amortization integer,
    Stock_based_compensation integer,
    Operating_Cash_Flow integer,
    Capital_Expenditure integer,
    Acquisitions_and_disposals integer,
    Investment_purchases_and_sales integer,
    Investing_Cash_flow integer,
    Issuance_or_repayment_of_debt integer,
    Issuance_or_buybacks_of_shares integer,
    Dividend_payments integer,
    Financing_Cash_Flow integer,
    Net_cash_flow integer,
    Free_Cash_Flow integer,
    NetCash_Marketcap integer,
    FOREIGN KEY (symbol) REFERENCES companies (symbol),
    UNIQUE(symbol, date)
);
"""

insert_cash_flow_data_sql = """ INSERT OR IGNORE INTO cash_flows (
    symbol,
    date, 
    Depreciation_Amortization,
    Stock_based_compensation,
    Operating_Cash_Flow,
    Capital_Expenditure,
    Acquisitions_and_disposals,
    Investment_purchases_and_sales,
    Investing_Cash_flow,
    Issuance_or_repayment_of_debt,
    Issuance_or_buybacks_of_shares,
    Dividend_payments,
    Financing_Cash_Flow,
    Net_cash_flow,
    Free_Cash_Flow,
    NetCash_Marketcap
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
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

def get_data_from_table(conn, table, company_symbol, data):
    ### pass data as list
    data = ', '.join(data)
    sql = f'SELECT {data} FROM {table} WHERE symbol={company_symbol}'
    cur = conn.cursor()
    values = cur.execute(sql)
    return values

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

def insert_balance_sheet_data(conn, balance_sheet):
    cur = conn.cursor()
    cur.execute(insert_balance_sheet_data_sql, balance_sheet)
    conn.commit()
    return cur.lastrowid

def insert_cash_flow_data(conn, cash_flows):
    cur = conn.cursor()
    cur.execute(insert_cash_flow_data_sql, cash_flows)
    conn.commit()
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