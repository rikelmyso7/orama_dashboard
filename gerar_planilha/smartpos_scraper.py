import os
import openpyxl
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from datetime import datetime, timedelta
from time import sleep

# Carrega variáveis de ambiente
load_dotenv()

EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")

pyautogui.FAILSAFE = False

def setup_browser():
    chrome_options = ChromeOptions()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.maximize_window()
    return browser

def login(browser):
    browser.get('https://app.smartpos.net.br')
    wait = WebDriverWait(browser, 20)
    
    wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(EMAIL)
    sleep(2)
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(SENHA)
    sleep(2)
    wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    sleep(2)

def navigate_to_vendas(browser):
    wait = WebDriverWait(browser, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div[4]/div[1]'))).click()
    sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[9]/div[2]/div/a[1]'))).click()
    sleep(2)

def set_date_range(browser, day: int):
    wait = WebDriverWait(browser, 20)
    campo_data = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker-wrapper")))
    campo_data.click()
    sleep(2)

    data_selector = f'//div[text()="{day}"]'
    wait.until(EC.element_to_be_clickable((By.XPATH, data_selector))).click()
    sleep(2)

    data_final = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div[2]/div[1]/form/div[1]/div[2]/div/div[1]/div/div')))
    data_final.click()
    sleep(2)

    wait.until(EC.element_to_be_clickable((By.XPATH, data_selector))).click()
    sleep(2)

def prepare_table(browser):
    wait = WebDriverWait(browser, 20)
    drop = wait.until(EC.element_to_be_clickable((By.ID, "pageDropDown")))
    drop.click()
    sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-page="100"]'))).click()
    sleep(2)

def scrape_vendas(browser, output_path: str):
    wait = WebDriverWait(browser, 20)
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Relatorio Vendas"
    sheet.append(["Código", "Data", "Vendedor", "Valor", "Dispositivo", "Forma de Pagamento", "Status"])

    pdvs = [
        "Brunholli", "Micheleto", "Travitália", "Da Roça", "Bendito Quintal",
        "Marquezim", "Sassafraz", "EVENTOS", "EVENTOS 2", "Fonte Basso"
    ]

    for _ in pdvs:
        try:
            vendedor_select = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div[2]/div[1]/form/div[1]/div[3]/label/div/div/div[2]/div[2]')))
            vendedor_select.click()
            sleep(2)

            pyautogui.press("down")
            sleep(2)
            pyautogui.press("enter")
            sleep(2)

            table = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))
            rows = table.find_elements(By.TAG_NAME, 'tr')

            for i in range(1, len(rows) + 1):
                try:
                    row_xpath = f'//tbody/tr[{i}]'
                    browser.find_element(By.XPATH, row_xpath).click()
                    sleep(2)

                    codigo = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sc-cFTihx"))).text
                    data = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/span/span'))).text
                    vendedor = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]'))).text
                    valor = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[9]/div[2]'))).text
                    dispositivo = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]'))).text
                    pagamento = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/div[1]/div/div[1]/span'))).text
                    status = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/span'))).text

                    sheet.append([codigo, data, vendedor, valor, dispositivo, pagamento, status])

                    close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div[1]/div/div[1]/div[1]/button')))
                    close_btn.click()
                    sleep(2)

                except Exception as e:
                    print(f"Erro no scraping linha {i}: {e}")

            pyautogui.hotkey('ctrl', 'home')
            sleep(2)
        except Exception as e:
            print(f"Erro no PDV: {e}")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    wb.save(output_path)
    print(f"Planilha salva em {output_path}")

def fechar_browser(browser):
    browser.quit()
