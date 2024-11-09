
def get_current_datetime():
    import datetime
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_datetime

def handle_get_current_datetime():
    report = get_current_datetime()
    return {"report": report}