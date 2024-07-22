# Google Image Extraction

This project uses Selenium to extract images from Google. The purpose of this small project is to download images from Google to assist in training machine learning models. Often, we need images to train models to recognize and classify various objects, and sometimes we lack the necessary images. This tool helps to automate the process of gathering such images.

## Setup

### Prerequisites

- Python 3.7
- virtualenv
- Download browser driver

### Installation

1. Clone this repository:

    ```bash
    git clone git@github.com:miguelzeph/download_images_google.git
    cd download_images_google
    ```

2. Create and activate a virtual environment with Python 3.7:

    ```bash
    virtualenv -p python3.7 venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configuration file:

    You can change the `config.yml` file and add the necessary environment variables.

    `P.S. Google has changed the image class for its images, beware the field **google.image_class**  might have to change one day.`

    ```yaml
    logger:
    level: INFO

    browser_driver:
    path: driver_Chromium/chromedriver
    download_image_path: images

    google:
    image_url: https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&
    # For reason of security, google always change
    # the image_class, so beware that this value
    # may have changed when you are executing the
    # script.
    image_class: YQ4gaf

    usr_agent:
    user-agent: "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    accept: "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    accept-charset: "ISO-8859-1,utf-8;q=0.7,*;q=0.3"
    accept-encoding: "none"
    accept-language: "en-US,en;q=0.8"
    connection: "keep-alive"
    ```

    Then, source the configuration file:

    ```bash
    source KLEIN_CONFIG=<your_config.yml_path>
    ```
### Downloading the Selenium WebDriver

To use Selenium, you need the driver corresponding to the browser you want to automate. Here are the steps to download the Chrome driver, for instance:

1. **Determine your Chrome version**:
    - Open Chrome and go to `chrome://settings/help` to see the browser version.

2. **Download the ChromeDriver**:

    - **For Chrome versions 115 and above**:
        - Use the following link to find the appropriate driver version: [ChromeDriver for versions 115+](https://googlechromelabs.github.io/chrome-for-testing/#stable).
        - Make sure to install the ChromeDriver version, not Chrome itself.

    - **For Chrome versions below 115**:
        - Use this link to find the appropriate driver version: [ChromeDriver for versions below 115](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).

3. **Add ChromeDriver to PATH**:
    - Extract the ChromeDriver and move it to a directory (make sure the name is **chromedriver**):
    ```bash
    # Move it to the directory
    src/driver_Chormium/chromedriver
    ```

    `P.S. In case you want to use other driver you can change the folder name and file name in the config.yml explaned above.`

### Running the Project

1. Ensure the virtual environment is activated:

    ```bash
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Run the main script:

    ```bash
    python main.py
    ```

### Notes

- Ensure that the ChromeDriver is in the PATH or provide the path directly in the Selenium code.
- This project has been tested with Python 3.7. Ensuring compatibility with other Python versions may require additional adjustments.
