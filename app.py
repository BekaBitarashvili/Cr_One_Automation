from flask import Flask, render_template, request, redirect, url_for, jsonify
from selenium import webdriver
from automation_parts.interface import TestWebsite
from automation_parts.auth import TestAuth
from automation_parts.restore_data import TestRestore
from automation_parts.user_settings import TestSettings
from automation_parts.currency_exchange import TestCurrency
from automation_parts.products import TestProducts

app = Flask(__name__)
test_website = TestWebsite()
test_auth = TestAuth()
test_restore = TestRestore()
test_settings = TestSettings()
test_currency = TestCurrency()
test_products = TestProducts()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/interface', methods=['GET', 'POST'])
def interface():
    try:
        test_website.setUpClass()
        test_website.test_01_crystal_logo()
        test_website.test_02_dark_mode()
        test_website.test_03_about()
        test_website.test_04_address()
        test_website.test_05_faq()
        test_website.test_06_facebook()
        test_website.test_07_youtube()
        test_website.test_08_linkedin()

        return jsonify({'status': 'success', 'message': 'სკრიპტი დასრულდა წარმატებით!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    try:
        test_auth.setUpClass()
        test_auth.test_01_incorrect_user_and_pass()
        test_auth.test_02_correct_user_and_incorrect_pass()
        test_auth.test_03_incorrect_user_and_correct_pass()
        test_auth.test_04_only_pass()
        test_auth.test_05_correct_user_and_pass()

        return jsonify({'status': 'success', 'message': 'სკრიპტი დასრულდა წარმატებით!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/restore', methods=['GET', 'POST'])
def restore():
    try:
        test_restore.setUpClass()
        test_restore.test_01_restore_data_button()
        test_restore.test_02_check_button()
        test_restore.test_03_check_inputs()
        test_restore.test_04_fill_inputs_correct_data()
        test_restore.test_05_type_6digit_code()
        test_restore.test_06_new_password()

        return jsonify({'status': 'success', 'message': 'სკრიპტი დასრულდა წარმატებით!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/user_settings', methods=['GET', 'POST'])
def user_settings():
    try:
        test_settings.setUpClass()
        test_settings.test_02_settings()
        test_settings.test_03_my_profile_section()
        test_settings.test_04_password_section()
        test_settings.test_05_history_section()
        test_settings.test_06_change_photo()
        test_settings.test_07_logout()

        return jsonify({'status': 'success', 'message': 'სკრიპტი დასრულდა წარმატებით!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/currency_exchange', methods=['GET', 'POST'])
def currency_exchange():
    try:
        test_currency.setUpClass()
        test_currency.test_01_login()
        test_currency.test_02_currency()
        test_currency.test_03_gel_to_usd()
        test_currency.test_04_eur_to_usd()

        return jsonify({'status': 'success', 'message': 'სკრიპტი დასრულდა წარმატებით!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/products', methods=['GET', 'POST'])
def products():
    try:
        test_products.setUpClass()
        test_products.test_01_login()
        test_products.test_02_loans()
        test_products.test_03_agreement_buttons()
        test_products.test_04_change_loan_name()

        return jsonify({'status': 'success', 'message': 'სკრიპტი დასრულდა წარმატებით!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


# error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
