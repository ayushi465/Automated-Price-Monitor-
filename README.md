# Automated Price Monitor


## Overview

The **Automated Price Monitor** is a tool designed to track and monitor prices of products from various e-commerce websites. It automates the process of checking prices, providing notifications when prices drop below a certain threshold. This tool is particularly useful for bargain hunters and consumers who want to purchase products at the best possible price.

## Features

- **Automated Price Tracking**: Monitors prices at regular intervals.
- **Threshold Notifications**: Alerts when prices fall below a set threshold.
- **Multi-Website Support**: Works with multiple e-commerce platforms.
- **User-Friendly Interface**: Easy to set up and use.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with the Automated Price Monitor, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/ayushi465/Automated-Price-Monitor-.git
    cd Automated-Price-Monitor
    ```

2. **Install dependencies**:

    Make sure you have Python and pip installed. Then, run the following command:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the Automated Price Monitor, follow these steps:

1. **Run the main script**:

    ```bash
    python main.py
    ```

2. **Configuration**:

    Update the `config.json` file with the product URLs and price thresholds you want to monitor.

    ```json
    {
        "products": [
            {
                "url": "https://example.com/product1",
                "threshold": 100.0
            },
            {
                "url": "https://example.com/product2",
                "threshold": 200.0
            }
        ]
    }
    ```

## Examples

Here's a basic example of how to use the price monitor:

1. **Add a product to the `config.json` file**:

    ```json
    {
        "products": [
            {
                "url": "https://example.com/product1",
                "threshold": 100.0
            }
        ]
    }
    ```

2. **Run the application**:

    ```bash
    python main.py
    ```

3. **Receive a notification**:

    ```
    Price drop alert! The price of the product at https://example.com/product1 is now 95.0, which is below your threshold of 100.0.
    ```

## Contributing

Contributions are welcome! If you'd like to contribute to the Automated Price Monitor, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
