def is_arithmetic_sequence(digits):
    if len(digits) < 2:
        return False
    common_diff = digits[1] - digits[0]
    for i in range(2, len(digits)):
        if digits[i] - digits[i - 1] != common_diff:
            return False
    return True

def count_favourite_times(D):
    from datetime import datetime, timedelta
    
    # Start time is 12:00
    start_time = datetime.strptime("12:00", "%H:%M")
    count = 0
    
    for minutes in range(D + 1):
        current_time = start_time + timedelta(minutes=minutes)
        hours = current_time.hour
        minutes = current_time.minute
        
        # Convert hours and minutes to digits
        digits = []
        if hours >= 10:
            digits.append(hours // 10)
        digits.append(hours % 10)
        if minutes >= 10:
            digits.append(minutes // 10)
        digits.append(minutes % 10)
        
        if is_arithmetic_sequence(digits):
            count += 1
    
    return count

# Example usage:
D = int(input())
print(count_favourite_times(D))
