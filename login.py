from sys import argv

def login(browser, callback = lambda browser : None) -> None:

    url_login_aluno = "https://qacademico.ifce.edu.br/qacademico/index.asp?t=1001"
    browser.get(url_login_aluno)

    matricula_input = browser.find_element_by_css_selector("input#txtLogin.formulario")
    senha_input = browser.find_element_by_css_selector("input#txtSenha.formulario")
    submit_button = browser.find_element_by_css_selector("input#btnOk.btnok")

    matricula_input.click()
    matricula_input.send_keys(argv[1])

    senha_input.click()
    senha_input.send_keys(argv[2])

    submit_button.click()

    callback(browser)