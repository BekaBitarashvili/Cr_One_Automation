from flask import Flask, render_template, request, redirect, url_for, jsonify
from selenium import webdriver
from automation_parts.interface import TestWebsite
from automation_parts.auth import TestAuth
from automation_parts.restore_data import TestRestore
from automation_parts.user_settings import TestSettings

app = Flask(__name__)
test_website = TestWebsite()
test_auth = TestAuth()
test_restore = TestRestore()
test_settings = TestSettings()


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
        test_restore.test_04_fill_inputs_incorrect_data()
        test_restore.test_05_fill_inputs_correct_personal()
        test_restore.test_06_fill_inputs_correct_mobile()
        test_restore.test_07_fill_inputs_correct_data()

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


# error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return '500 Internal Server Error'


if __name__ == '__main__':
    app.run(debug=True)
