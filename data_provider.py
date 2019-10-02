from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib
import json
import db_handler
import datetime

# path to local database
database = "./stock_db.db"

# implements API calls as backup (only works for US traded stocks)
def get_income_statements(company_short):
    api_url_income_statement = f'https://financialmodelingprep.com/api/v3/financials/income-statement/{company_short}'

    response = requests.get(api_url_income_statement)
    if response.status_code == 200:
        income_statement_data = json.loads(response.text)
        try:
            historical_is = income_statement_data['financials']
            print(f'Historical income statement data of {company_short} found for the last {len(historical_is)} years.')
            print("committing to DB ...")

            # connect to DB if create income statements table, if not exists, then commit data
            conn = db_handler.create_connection("./stock_db.db")
            db_handler.create_table(conn, db_handler.create_income_statements_table)
            for year_index, y in enumerate(historical_is):
                data_list = []
                data_list.append(company_short)
                # this year is a JSON object
                this_year = historical_is[year_index]
                # go through all data that is relevant and append to list to pass to DB
                data_list.append(this_year["date"])
                data_list.append(this_year["Revenue"])
                data_list.append(this_year["Revenue Growth"])
                data_list.append(this_year["Cost of Revenue"])
                data_list.append(this_year["Gross Profit"])
                data_list.append(this_year["R&D Expenses"])
                data_list.append(this_year["SG&A Expense"])
                data_list.append(this_year["Operating Expenses"])
                data_list.append(this_year["Operating Income"])
                data_list.append(this_year["Interest Expense"])
                data_list.append(this_year["Earnings before Tax"])
                data_list.append(this_year["Income Tax Expense"])
                data_list.append(this_year["Net Income"])
                data_list.append(this_year["EPS"])
                data_list.append(this_year["Dividend per Share"])
                data_list.append(this_year["Gross Margin"])
                data_list.append(this_year["EBITDA Margin"])
                data_list.append(this_year["EBIT Margin"])
                data_list.append(this_year["Profit Margin"])
                data_list.append(this_year["Free Cash Flow margin"])
                data_list.append(this_year["EBITDA"])
                data_list.append(this_year["EBIT"])
                data_list.append(this_year["Earnings Before Tax Margin"])
                data_list.append(this_year["Net Profit Margin"])
                # pass to commit to DB
                db_handler.insert_income_statement_data(conn, data_list)
            print("Income statement data committed successfully.")
            db_handler.close_connection(conn)
            return True
        except:
            raise Exception("The API call went wrong. No data committed to DB.")
    else:
        raise Exception("Could not retrieve company data from API.")

def get_balance_sheets(company_short):
    api_url_balance_sheet = f'https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/{company_short}'
    response = requests.get(api_url_balance_sheet)
    if response.status_code == 200:
        balance_sheet_data = json.loads(response.text)
        try:
            historical_bs = balance_sheet_data['financials']
            print(f'Historical balance sheet data of {company_short} found for the last {len(historical_bs)} years.')
            print("committing to DB ...")

            # connect to DB if create income statements table, if not exists, then commit data
            conn = db_handler.create_connection("./stock_db.db")
            db_handler.create_table(conn, dv)
            for year_index, y in enumerate(historical_bs):
                data_list = []
                data_list.append(company_short)
                # this year is a JSON object
                this_year = historical_bs[year_index]
                # go through all data that is relevant and append to list to pass to DB
                
                # pass to commit to DB
                # db_handler.insert_income_statement_data(conn, data_list)
            print("Data committed successfully.")
        except:
            print("That didn't work.")
    else:
        print("Could not retrieve data from API.")

def get_key_metrics(company_short):
    api_url_metrics = f'https://financialmodelingprep.com/api/v3/company-key-metrics/{company_short}'

    response = requests.get(api_url_metrics)
    if response.status_code == 200:
        metrics_data = json.loads(response.text)
        try:
            historical_is = metrics_data['metrics']
            print(f'Metrics data found for the last {len(historical_is)} years.')
            return historical_is
        except:
            raise Exception("There are no records for the company under the symbol you provided.")
    else:
        raise Exception("Could not retrieve company data from API.")