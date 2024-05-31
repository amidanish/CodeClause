def get_exchange_rate(currency_name):
    exchange_rates = {
        'US Dollar': 1.0,
        'Indian Rupee': 0.012,
        'Japanese Yen': 0.0091,
        'Euro': 1.1,
        'British Pound': 1.3,
        'Australian Dollar': 0.74,
        'Canadian Dollar': 0.78,
        'Swiss Franc': 1.09,
        'Chinese Yuan': 0.16,
        'Swedish Krona': 0.11,
        'Norwegian Krone': 0.12,
        'South Korean Won': 0.00085,
        'Singapore Dollar': 0.74,
        'Hong Kong Dollar': 0.13,
        'New Zealand Dollar': 0.71,
        'Mexican Peso': 0.052,
        'Brazilian Real': 0.19,
        'South African Rand': 0.065,
        'Russian Ruble': 0.013,
        'Turkish Lira': 0.13,
        'Argentine Peso': 0.012,
        'Chilean Peso': 0.0013,
        'Colombian Peso': 0.00027,
        'Egyptian Pound': 0.064,
        'Israeli Shekel': 0.31,
        'Malaysian Ringgit': 0.24,
        'Nigerian Naira': 0.0026,
        'Philippine Peso': 0.018,
        'Thai Baht': 0.032,
        'Indonesian Rupiah': 0.000069,
        'Pakistani Rupee': 0.0064,
        'Bangladeshi Taka': 0.012,
        'Vietnamese Dong': 0.000043,
        'Ukrainian Hryvnia': 0.036,
        'Polish Zloty': 0.26,
        'Czech Koruna': 0.045,
        'Hungarian Forint': 0.0032,
        'Romanian Leu': 0.24,
        'Croatian Kuna': 0.16,
        'Bulgarian Lev': 0.61,
        'Icelandic Krona': 0.0076,
        'Serbian Dinar': 0.010,
        'Kazakhstani Tenge': 0.0023,
        'Georgian Lari': 0.38,
        'Armenian Dram': 0.0021,
        'Azerbaijani Manat': 0.59,
        'Belarusian Ruble': 0.38,
        'Macedonian Denar': 0.019
    }

    if currency_name in exchange_rates:
        return exchange_rates[currency_name]
    else:
        raise ValueError(f"No data available for {currency_name}")

def currency_conversion():
    while True:
        amount = float(input('Enter the amount to convert: '))
        source_currency = input('Enter the currency you are converting from (e.g., US Dollar): ')
        target_currency = input('Enter the currency you want to convert to (e.g., Euro): ')

        try:
            source_rate = get_exchange_rate(source_currency)
            target_rate = get_exchange_rate(target_currency)

            if source_currency == target_currency:
                print(f"{amount} {source_currency} is exactly {amount} {target_currency}")
            else:
                amount_in_usd = amount * source_rate
                converted_amount = amount_in_usd / target_rate
                print(f"{amount} {source_currency} converts to {converted_amount:.2f} {target_currency}")

        except ValueError as error:
            print(error)

        another_conversion = input("Do you want to convert another amount? (yes/no): ").lower()
        if another_conversion != 'yes':
            print("Thank you for using the currency converter!")
            break

currency_conversion()
