from gerar_planilha import smartpos_scraper
from datetime import datetime, timedelta

def main():
    data = datetime.now() - timedelta(days=0)
    day = int(data.strftime("%d"))

    browser = smartpos_scraper.setup_browser()
    try:
        smartpos_scraper.login(browser)
        smartpos_scraper.navigate_to_vendas(browser)
        smartpos_scraper.set_date_range(browser, day)
        smartpos_scraper.prepare_table(browser)

        output_path = f'output/relatorio_vendas_{data.strftime("%d_%m")}.xlsx'
        smartpos_scraper.scrape_vendas(browser, output_path)
    finally:
        smartpos_scraper.fechar_browser(browser)

if __name__ == "__main__":
    main()
