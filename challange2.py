def convert_to_24_hour(hour, minute, period):
    if period.lower() == "pm" and hour != 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0

    return "{:02d}{:02d}".format(hour, minute)

# Example usage:
hour = 8
minute = 30
period = "am"

result = convert_to_24_hour(hour, minute, period)
print(result)
