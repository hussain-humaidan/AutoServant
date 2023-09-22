from hijri_converter import Gregorian


# Convert a Gregorian date to Hijri
def convert(year, month, day):
    hijri_Date = Gregorian(year, month, day).to_hijri()

    # Convert Hijri month from int to string
    hijri_month = hijri_Date.month_name()
    Date = [hijri_Date.year, hijri_month, hijri_Date.day]

    hijri_year = Date[0]
    hijri_month = Date[1]
    hijri_day = Date[2]

    return hijri_year, hijri_month, hijri_day
