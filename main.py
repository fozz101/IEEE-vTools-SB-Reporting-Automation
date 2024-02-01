import time
from selenium.webdriver.common.by import By
import pandas as pd
from selenium import webdriver

from selenium.webdriver.chrome.options import Options



universities = [
    "STB64613",
    "STB12541",
    "STB14511",
    "STB03301",
    "STB13021",
    "STB10213",
    "STB09861",
    "STB12331",
    "STB09511",
    "STB10222",
    "STB39501",
    "STB11516",
    "STB13271",
    "STB17411",
    "STB10225",
    "STB11413",
    "STB60168044",
    "STB10019",
    "STB11321",
    "STB99999",
    "STB99079",
    "STB16991",
    "STB64692",
    "STB10060",
    "STB10056",
    "STB12511",
    "STB20136",
    "STB20236",
    "STB10106",
    "STB16311",
    "STB39451",
    "STB99105",
    "STB13281",
    "STB10057",
    "STB17201",
    "STB13161",
    "STB60214145",
    "STB60122624",
    "STB10024",
    "STB60211845",
    "STB10112",
    "STB14025",
    "STB66436",
    "STB15160",
    "STB64634"
]

universities = [
    "STB64613 - ESPRIT",
    "STB12541 - National Institute of Applied Sciences & Technology",
    "STB14511 - National School of Electronics & Telecoms of Sfax",
    "STB03301 - National Engineering School of Sfax (ENIS)",
    "STB13021 - Faculty of Science of Tunis",
    "STB10213 - Higher School of Sciences & Tech of Hammam Sousse",
    "STB09861 - Higher School of Communication of Tunis (Sup'Com)",
    "STB12331 - National Engineering School of Carthage",
    "STB09511 - National School of Computer Science ENSI",
    "STB10222 - Higher Inst of Informatics & Multimedia of Sfax",
    "STB39501 - Higher Institute of Informatics Mahdia",
    "STB11516 - Higher Inst Informatics & Mathematics of Monastir",
    "STB13271 - Higher National Engineering School of Tunis",
    "STB17411 - Ecole Nationale D'Ingenieurs De Tunis",
    "STB10225 - Higher Inst of Applied & Tech Sciences of Mateur",
    "STB11413 - International Multidisciplinary School",
    "STB60168044 - Higher Inst of Information Technologies & Comm.",
    "STB10019 - Ecole Polytechnique de Sousse",
    "STB11321 - National Engineering School of Sousse (ENISo)",
    "STB99999 - Faculty of Sciences of Sfax",
    "STB99079 - South Mediterranean University",
    "STB16991 - Higher Inst of Applied Science & Tech of Sousse",
    "STB64692 - Institute of Technological Studies of Bizerte",
    "STB10060 - National Agronomic Institute of Tunisia",
    "STB10056 - Higher Institute of Computer Science",
    "STB12511 - National Engineering School of Gabes",
    "STB20136 - Higher Institute of Technological Studies-Djerba",
    "STB20236 - TEK-UP Higher School of Technologies & Engineering",
    "STB10106 - International Institute of Technology",
    "STB16311 - Private University of Tunis",
    "STB39451 - SESAME University",
    "STB99105 - Higher Institute of Industrial Management of Sfax",
    "STB13281 - National Engineering School of Monastir",
    "STB10057 - Higher Institute of Technological Studies of Rades",
    "STB17201 - Natl School of Advanced Sci & Tech of Borj Cedria",
    "STB13161 - National Engineering School of Bizerte",
    "STB60214145 - Manouba School of Engineering",
    "STB60122624 - Higher Inst. of Computer Science Multimedia Gabes",
    "STB10024 - Private Polytechnic School-Monastir",
    "STB60211845 - ESPIN University",
    "STB10112 - Polytech Sfax",
    "STB14025 - Faculty of Sciences of Bizerte",
    "STB66436 - Higher Institute of Tech. Studies of Kairouan",
    "STB15160 - Higher Institute of Technological Studies ISET'COM",
    "STB64634 - Private Higher School of Eng. & Applied Tech"
]


chrome_options = Options()
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
sbrUrl = "https://sbr.vtools.ieee.org/tego_/plans/search?_sub=true&school=&region=R8&section=R80114&year=2024&commit=Search"


driver.get(sbrUrl)

email = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")

signInButton = driver.find_element(By.ID,"modalWindowRegisterSignInBtn")

email.send_keys(input("email= "))
password.send_keys(input("password= "))

signInButton.click()
time.sleep(6)

df = pd.read_excel("SBs rebate eligibility.xlsx")

df['SB reporting'] = None
for index, row in df.iterrows():

    for sb in universities:
        sb = sb.split(" - ")[0]
        if sb in driver.page_source and sb in row['Student Branch']:
            df.at[index, 'SB reporting'] = "Yes"
            break

        if sb not in driver.page_source and sb in row['Student Branch']:
            df.at[index, 'SB reporting'] = "No"
            break



df.to_excel("your_excel_file_with_SB_column.xlsx", index=False)


result = []
for sb in universities:
    sb = sb.split(" - ")[0]
    didSBreport = {}
    if sb in driver.page_source:
        didSBreport[sb] = "Yes"
        print(sb + " Yes")
    else:
        didSBreport[sb] = "No"
        print(sb + " No")

    result.append(didSBreport)

print(result)
driver.quit()


