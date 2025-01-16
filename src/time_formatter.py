def format_time(minutes):
    if not isinstance(minutes, (int, float)) or minutes < 0:
        raise ValueError("Input must be a non-negative number")
    
    hours = int(minutes // 60)
    remaining_minutes = int(minutes % 60)
    
    if hours == 0:
        return f"{remaining_minutes}m"
    elif remaining_minutes == 0:
        return f"{hours}h"
    else:
        return f"{hours}h {remaining_minutes}m"