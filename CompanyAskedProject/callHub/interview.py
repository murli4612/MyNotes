import csv
import pytz
import phonenumbers
from phonenumbers import timezone as phonetimezone
from datetime import datetime, timedelta

CALL_DURATION = 3  # minutes
CALL_WINDOW_START = 9  # 9 AM
CALL_WINDOW_END = 20   # 8 PM

def parse_phone_number(phone_str):
    try:
        parts = phone_str.strip().split('-')
        if len(parts) < 3:
            return None
        country_code = parts[0]
        area_code = parts[1]
        subscriber = ''.join(parts[2:])
        return f"+{country_code}{area_code}{subscriber}"
    except Exception as e:
        print(f"Error parsing phone: {phone_str} -> {e}")
        return None

def get_valid_timezones(phone_number):
    try:
        parsed = phonenumbers.parse(phone_number)
        time_zones = phonetimezone.time_zones_for_number(parsed)
        
        if not time_zones:
            region = phonenumbers.region_code_for_number(parsed)
            if region:
                time_zones = pytz.country_timezones.get(region.upper(), [])
        
        valid_timezones = []
        for tz_name in time_zones:
            try:
                pytz.timezone(tz_name)
                valid_timezones.append(tz_name)
            except pytz.UnknownTimeZoneError:
                continue
        
        return valid_timezones if valid_timezones else None
    except Exception as e:
        print(f"Error getting timezone for {phone_number}: {e}")
        return None

def is_within_call_window(current_utc, timezones):
    for tz_name in timezones:
        try:
            tz = pytz.timezone(tz_name)
            local_time = current_utc.astimezone(tz)
            if not (CALL_WINDOW_START <= local_time.hour < CALL_WINDOW_END):
                return False
        except Exception as e:
            print(f"Error checking timezone {tz_name}: {e}")
            return False
    return True

def next_valid_call_time(current_utc, timezones):
    next_times = []
    for tz_name in timezones:
        try:
            tz = pytz.timezone(tz_name)
            local_time = current_utc.astimezone(tz)
            
            today_start = local_time.replace(
                hour=CALL_WINDOW_START, 
                minute=0, 
                second=0, 
                microsecond=0
            )
            
            if local_time < today_start:
                next_time = today_start
            else:
                next_time = today_start + timedelta(days=1)
            
            next_times.append(next_time.astimezone(pytz.UTC))
        except pytz.UnknownTimeZoneError:
            continue
    
    if not next_times:
        return current_utc + timedelta(days=1) 
    
    return max(next_times)

def calculate_total_time(phone_numbers_csv, start_time_utc_str):
    time_str = start_time_utc_str.replace('UTC', '').strip()
    try:
        start_time_naive = datetime.strptime(time_str, "%H:%M:%S")
        start_time_utc = pytz.UTC.localize(start_time_naive.replace(
            year=datetime.utcnow().year,
            month=datetime.utcnow().month,
            day=datetime.utcnow().day
        ))
    except Exception as e:
        print(f"Error parsing start time: {e}")
        return None
    phone_numbers = []
    with open(phone_numbers_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                phone = parse_phone_number(row[0])
                if phone:
                    timezones = get_valid_timezones(phone)
                    if timezones:
                        phone_numbers.append({
                            'original': row[0],
                            'formatted': phone,
                            'timezones': timezones
                        })

    if not phone_numbers:
        print("No valid phone numbers found")
        return None

    current_time = start_time_utc
    total_call_time = 0
    total_wait_time = 0
    queue = phone_numbers.copy()

    while queue:
        called = False
        for i in range(len(queue)):
            entry = queue[i]
            if is_within_call_window(current_time, entry['timezones']):
                total_call_time += CALL_DURATION
                current_time += timedelta(minutes=CALL_DURATION)
                queue.pop(i)
                called = True
                break

        if not called:
            next_time = None
            for entry in queue:
                entry_next_time = next_valid_call_time(current_time, entry['timezones'])
                if next_time is None or entry_next_time > next_time:
                    next_time = entry_next_time
            
            if next_time is None:
                next_time = current_time + timedelta(days=1)
            
            wait_minutes = (next_time - current_time).total_seconds() / 60
            total_wait_time += wait_minutes
            current_time = next_time

    total_minutes = total_call_time + total_wait_time
    days = total_minutes // (24 * 60)
    remaining_hours = (total_minutes % (24 * 60)) // 60

    return {
        'agent_call_duration': int(total_call_time),
        'agent_wait_duration': int(total_wait_time),
        'total_time_in_days_hours': f"{int(days)} days and {int(remaining_hours)} hours"
    }

if __name__ == "__main__":
    result = calculate_total_time(
        phone_numbers_csv="random numbers for assignment.csv",
        start_time_utc_str="21:30:00 UTC"
    )
    print(result)